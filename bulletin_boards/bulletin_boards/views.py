import logging

# import pytz
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .filters import NewsFilter
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
        return context

    def article(self, request):
        return redirect('/')


class CommentCreate(CreateView):  # LoginRequireMixin,
    model = Comment
    template_name = 'article_detail.html'   # !!!!
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.comment_user = self.request.user
        comment.comment_post_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_id'] = self.kwargs['pk']
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'post.html'
    # context_object_name = 'articles'


# class ArticleDetail(CommentCreate, DetailView):
#     permission_required = ('add_article',)
#     # Модель всё та же, но мы хотим получать информацию по отдельному товару
#     model = Article
#     # Используем другой шаблон —
#     # post_detail.html
#     template_name = 'post.html'
#     # Название объекта, в котором будет выбранный пользователем продукт
#     context_object_name = 'articles'
#     pk_url_kwarg = 'pk'


# class Search(ListView):
#     model = Post
#     template_name = 'search.html'
#     context_object_name = 'posts'
#     ordering = '-post_time'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = NewsFilter(self.request.GET, queryset)
#         if self.request.GET:
#             return self.filterset.qs
#         return Post.objects.none()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         return context


# @login_required
# class PostCreate(PermissionRequiredMixin, CreateView):
#     permission_required = ('news.add_post',)
#     form_class = PostForm
#     model = Article
#     template_name = 'news/post_create.html'
#
#     # context_object_name = 'post_create'
#
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         if self.request.path == '/news_create/':
#             post.post.news = 'NE'
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('post', kwargs={'pk': self.object.pk})

# def get_form_kwargs(self):
#     kwargs = super().get_form_kwargs()
#     if self.request.user != kwargs['instance'].user:
#         return self.handle_no_permission()
#     return kwargs


class ArticleCreate(LoginRequiredMixin, CreateView):
    permission_required = ('add_article',)
    raise_exception = True
    form_class = ArticleForm
    model = Article
    template_name = 'article/articles_create.html'

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     if self.request.path == '/articles_create/':
    #         post.post.news = 'AR'
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('delete_article',)
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('article')

    def get_success_url(self):
        return reverse_lazy('article')


class ArticleUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('bulletin_boards.article_change',)
    form_class = EditForm
    model = Article
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article')

# class ArticleUpdate(PermissionRequiredMixin, UpdateView):
#     permission_required = ('articles.change_article',)
#     form_class = ArticleForm
#     model = Article
#     template_name = 'article/articles_edit.html'
#
#     def get_success_url(self):
#         return reverse_lazy('article')

# class CategoryListView(NewsList):
#     model = Article
#     template_name = 'news/category_list.html'
#     context_object_name = 'category_news_list'
#
#     def get_queryset(self):
#         self.category = get_object_or_404(Category, id=self.kwargs['pk'])
#         queryset = Article.objects.filter(category=self.category).order_by('-post_time')
#         return queryset
#
#     def get_context_data(self, **kwargs):  # для кнопки подписаться
#         context = super().get_context_data(**kwargs)
#         context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
#         context['category'] = self.category
#         return context


# @login_required
# def upgrade_me(request):
#     user = request.user
#     premium_group = Group.objects.get(name='authors')
#     if not request.user.groups.filter(name='authors').exists():
#         premium_group.user_set.add(user)
#     return redirect('/news')


# @login_required
# def subscribe(request, pk):
#     user = request.user
#     category = Category.objects.get(id=pk)
#     category.subscribers.add(user)
#
#     message = 'Вы успешно подписались на рассылку новостей категории'
#     return render(request, 'news/subscribe.html', {'category': category, 'message': message})


# rest
# def get_article(_, pk):
#     article = Article.objects.get(pk=pk)
#     return HttpResponse(content=article, status=200)
#
#
# def get_articles(_):
#     articles = Article.objects.all()
#     return HttpResponse(content=articles, status=200)
#
#
# def create_article(request):
#     body = json.loads(request.body.decode('utf-8'))
#     article = Article.objects.create(
#         title=body['title'],
#         text=body['text']
#     )
#     # article.save()
#     # data = {'title': article.title, 'text': article.text}
#     return HttpResponse(content=article, status=201)
#
#
# def edit_article(request, pk):
#     body = json.loads(request.body.decode('utf-8'))
#     article = Article.objects.get(pk=pk)
#     for attr, value in body.items():  # редактирование объекта
#         setattr(article, attr, value)
#     article.save()
#     data = {'title': article.title, 'text': article.text}
#     return HttpResponse(content=data, status=200)
#
#
# def delete_article(_, pk):
#     Article.objects.get(pk=pk).delete()
#     return HttpResponse(status=204)
