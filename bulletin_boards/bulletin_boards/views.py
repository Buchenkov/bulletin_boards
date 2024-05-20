import logging

# import pytz
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .filters import NewsFilter, PostFilter
from .forms import ArticleForm, CommentForm, EditForm
# from .forms import PostForm, ArticleForm
from .models import *

logger = logging.getLogger(__name__)


def index(request):  # при переходе по определённому урлу
    logger.info('INFO')
    return redirect('')


class ArticleList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Article
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'article.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'articles'
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-post_time'
    paginate_by = 10  # количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        # print(context)
        return context

    def article(self, request):
        return redirect('/')


# class CommentList(ListView):
#     # Указываем модель, объекты которой мы будем выводить
#     model = Comment
#     # Указываем имя шаблона, в котором будут все инструкции о том,
#     # как именно пользователю должны быть показаны наши объекты
#     template_name = 'article.html'
#     # Это имя списка, в котором будут лежать все объекты.
#     # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
#     context_object_name = 'Comments'
#     # Поле, которое будет использоваться для сортировки объектов
#     # ordering = '-post_time'
#     paginate_by = 10  # количество записей на странице


# class ReplyCreate(LoginRequiredMixin, CreateView):
#     # form_class = RepleForm
#     model = UserResponse
#     # template_name =
#
#     def form_valid(self, form):
#         reply = form.save(commit=False)
#         article = get_object_or_404(Article, id=self.kwargs['pk'])
#         form.instance.user = self.request.user
#         form.instance.article = article
#         reply.save()
#         author = User.objects.get(pk=article.author_id)
#         send_mail(
#             subject=f'Отклик на объявление!',
#             message=f'На ваше объявление: "{article}" был оставлен отклик: "{reply.reple_text}" пользователем {self.request.user}',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[author.email],
#         )
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         article = get_object_or_404(Article, id=self.kwargs['pk'])
#         context['article'] = article
#         return context


class CommentCreate(CreateView):  # LoginRequireMixin,
    model = Comment
    template_name = 'post.html'
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.comment_user = self.request.user
        comment.comment_post_id = self.kwargs['pk']
        # comment.status = 0
        article = get_object_or_404(Article, id=self.kwargs['pk'])
        author = User.objects.get(pk=article.author_id)
        comment.save()
        send_mail(
            subject=f'Отклик на объявление!',
            message=f'На ваше объявление: "{article.title}" был оставлен отклик: {comment.text} пользователем: {self.request.user}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[author.email],
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_id'] = self.kwargs['pk']
        # print("INFORM!!!! ", context)
        return context

    def get_success_url(self):
        return reverse_lazy('article')


class ArticleDetail(DetailView, CommentCreate):
    model = Article
    template_name = 'post.html'
    # context_object_name = 'articles'


def comment_add(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.status = True  # Изменяем статус на "Подтвержден"
    print('! ! !', comment)
    # article = get_object_or_404(Comment, pk=pk)
    author = User.objects.get(pk=comment.comment_user_id)
    send_mail(
        subject=f'Отклик на объявление!',
        message=f'Ваш отклик: "{comment.text}" на объявление {comment.comment_post.author}: '
                f'{comment.comment_post.title} - принят!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[author.email],
    )
    comment.save()
    return redirect('profile')


# class CommentAdd(UpdateView, CommentCreate):
#     permission_required = ('bulletin_boards.change_comment',)
#     model = Comment
#     template_name = 'article/comment_add.html'
#     # context_object_name = 'articles'
#
#     # def get_context_data(self, **kwargs):
#     #     response = get_object_or_404(Comment, id=self.kwargs['pk'])
#     #     response.status = 1  # Изменяем статус на "Подтвержден"
#     #     response.save()
#     #     return redirect('account/profile')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['id'] = Comment.objects.get(pk=self.kwargs.get('pk')).id
#         context['status'] = 1
#         print(context['id'], context['status'])
#         return context
#
#     def form_valid(self, form):
#         post = form.save(commit=True)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('article')


class ArticleCreate(CreateView):  # LoginRequiredMixin, PermissionRequiredMixin,
    permission_required = ('bulletin_boards.add_article',)
    # raise_exception = True  # вместо перенаправлений, можно генерировать страницу с кодом 403 – доступ запрещен.
    form_class = ArticleForm
    model = Article
    template_name = 'article/articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article')


class ArticleDelete(LoginRequiredMixin, DeleteView):
    permission_required = ('bulletin_boards.delete_article',)
    model = Article
    template_name = 'article/article_delete.html'

    # success_url = reverse_lazy('article')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Article.objects.get(pk=self.kwargs.get('pk')).author
        # print(context)
        return context

    def get_success_url(self):
        return reverse_lazy('article')


class CommentDelete(LoginRequiredMixin, DeleteView):
    permission_required = ('bulletin_boards.delete_comment',)
    model = Comment
    template_name = 'article/comment_delete.html'

    # success_url = reverse_lazy('article')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author'] = Comment.objects.get(pk=self.kwargs.get('pk'))   # .author
    #     print(context)
    #     return context

    def get_success_url(self):
        return reverse_lazy('profile')


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    permission_required = ('bulletin_boards.change_article',)
    form_class = EditForm
    model = Article
    template_name = 'articles_edit.html'

    # fp = Article(file=form.clened_data['data'])
    # fp.save()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Article.objects.get(pk=self.kwargs.get('pk')).author
        # print(context)
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article')


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    # success_url = '/accounts/login/'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'account/account_inactive.html')
        return redirect('account_login')


class ProfileView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'account/profile.html'
    context_object_name = 'comments'  # для итерации в profile.html

    def get_queryset(self):  # original
        queryset = Comment.objects.filter(comment_post__author_id=self.request.user.id)
        self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Comment.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
