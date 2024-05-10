from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'text', 'category', 'post_time', 'upload']


# class CategoryAdmin(TranslationAdmin):
#     model = Category
#
#
# class MyModelAdmin(TranslationAdmin):
#     model = Post


# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(User)
