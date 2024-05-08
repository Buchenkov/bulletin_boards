from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter, CharFilter, ModelChoiceFilter, \
    ChoiceFilter

from .models import Article


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):
    category = ChoiceFilter(field_name='category',
                            choices=Article.TYPE,
                            label='Category',
                            empty_label='Select a category')
    added_after = DateTimeFilter(
        field_name='post_time',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Article
        # fields = ['title', 'category', 'added_after']
        fields = {
            'title': ['icontains'],
            # 'category': ['exact'],
            # 'post_time': ['gt'],
        }



# class NewsFilter(FilterSet):
#     title = CharFilter(
#         lookup_expr='icontains',
#         field_name='title',
#         label='Заголовок',
#     )
#
#     category = ModelChoiceFilter(
#         field_name='category',
#         lookup_expr='exact',
#         queryset=Category.objects.all(),
#         label='Категория',
#         empty_label='Любая',
#     )
#     date = DateTimeFilter(
#         field_name='post_time',
#         lookup_expr='gt',
#         label='Дата',
#         widget=DateTimeInput(
#             attrs={'type': 'date'},
#         ),
#     )
#
#     class Meta:
#         model = Post
#         fields = ['title', 'date', 'category']





