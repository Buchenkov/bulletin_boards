from django.contrib import admin

from .models import *
# from modeltranslation.admin import TranslationAdmin    # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)


# напишем функцию для обнуления новостей
# def nullfy_quantity(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
#     queryset.update(quantity=0)
# nullfy_quantity.short_description = 'Обнулить товары' # описание для более понятного представления в админ панеле задаётся, как будто это объект


# создаём новый класс для представления новостей в админке
# class PostAdmin(admin.ModelAdmin):
#     # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
#     # list_display = [field.name for field in
#     #                 Category._meta.get_fields()]  # генерируем список имён всех полей для более красивого отображения
#     # def subject_post(self, obj):
#     #     return ', '.join([category.category_name for category in obj.category_post_many.all()])
#
#     list_display = ('author', 'title', 'text', 'rating', 'subject_post', 'post_time')  # оставляем только имя и цену товара
#     # list_filter = ('author', 'title', 'text', 'rating', 'post_type', 'post_time')  # добавляем примитивные фильтры в нашу админку
#     list_filter = ('post_time', 'author')
#     search_fields = ('author__user__username', 'category__category_name')  # тут всё очень похоже на фильтры из запросов в базу
#     actions = [nullfy_quantity]  # добавляем действия в список
#
#     def subject_post(self, obj):
#         return ', '.join([category.category_name for category in obj.category.all()])


# class CategoryAdmin(TranslationAdmin):
#     model = Category


# class MyModelAdmin(TranslationAdmin):
#     model = Post


# Register your models here.
# admin.site.register(Category)
admin.site.register(Article)
# admin.site.register(Author)
admin.site.register(Comment)
# admin.site.register(PostCategory)
# admin.site.register(Subscription)
# admin.site.register(Search)
