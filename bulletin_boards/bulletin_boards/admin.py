from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import *


class ArticleAdminForm(forms.ModelForm):
    upload = forms.CharField(widget=CKEditorUploadingWidget())
    # """Форма с виджетом ckeditor"""
    # description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    # description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


# @admin.register(Category)
# class CategoryAdmin(TranslationAdmin):
#     """Категории"""
#     list_display = ("name", "url")
#     list_display_links = ("name",)


# class Comment(admin.TabularInline):
#     """Отзывы на странице фильма"""
#     model = Comment
#     extra = 1
#     readonly_fields = ("comment_user", "comment_post")


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


# class PostAdmin(admin.ModelAdmin):
#     fields = ['author', 'title', 'text', 'category', 'post_time', 'upload']


# class CategoryAdmin(TranslationAdmin):
#     model = Category
#
#
# class MyModelAdmin(TranslationAdmin):
#     model = Post 560


# Register your models here.
admin.site.register(Article, ArticleAdmin)
# admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(User)
