import logging

import form
# import pytz
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, TemplateView

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
    template_name = 'article_detail.html'  # !!!!
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


class ArticleCreate(LoginRequiredMixin, CreateView):
    permission_required = ('add_article',)
    raise_exception = True
    form_class = ArticleForm
    model = Article
    template_name = 'article/articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        return super().form_valid(form)

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
    # fp = Article(file=form.clened_data['data'])
    # fp.save()

    def form_valid(self, form):
        post = form.save(commit=False)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article')


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'accounts/invalid_code_html')
        return redirect('account_login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
