from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Article(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Кестгиеры'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()   # !
    category = models.CharField(max_length=20, choices=TYPE, default='tank')
    post_time = models.DateTimeField(auto_now_add=True)  # автоматически добавляемая дата и время создания;
    upload = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return f'{self.title}: {self.text[:20]}'

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class UserResponse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Comment(models.Model):
    comment_post = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Комментарии')  # связь с моделью Article;
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', verbose_name='Автор')  # связь с моделью User
    text = models.TextField(verbose_name='Описание')  # текст комментария;
    comment_time = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')  # дата и время создания комментария;
    status = models.BooleanField(default=False, verbose_name='статус')

    def __str__(self):
        return f'{self.comment_user}: {self.text}'

    def get_absolut_url(self):
        return reverse('article_detail', kwargs={'pk': self.comment_post_id})

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['id']


# class Subscription(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='subscriptions',)
#     article = models.ForeignKey(to='Article', on_delete=models.CASCADE, related_name='subscriptions',)
