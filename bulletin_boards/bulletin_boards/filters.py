from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ChoiceFilter

from .models import Article, Comment


class PostFilter(FilterSet):
    class Meta:
        model = Comment
        fields = {
            'comment_post'
        }

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['comment_post'].queryset = Article.objects.filter(author_id=kwargs['request'])


# Создаем свой набор фильтров для модели.
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

        fields = {
            'title': ['icontains'],
        }
