from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import *


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    # """Форма с виджетом ckeditor"""
    # description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    # description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(User)
