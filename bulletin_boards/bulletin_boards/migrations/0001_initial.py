# Generated by Django 4.2.11 on 2024-05-08 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('tank', 'Танки'), ('heal', 'Хилы'), ('dd', 'ДД'), ('buyers', 'Торговцы'), ('gildemaster', 'Гилдмастеры'), ('quest', 'Кестгиеры'), ('smith', 'Кузнецы'), ('tanner', 'Кожевники'), ('potion', 'Зельевары'), ('spellmaster', 'Мастера заклинаний')], default='tank', max_length=20)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(blank=True, upload_to='uploads/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_boards.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('status', models.BooleanField(default=False, verbose_name='статус')),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulletin_boards.article', verbose_name='Комментарии')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ['id'],
            },
        ),
    ]
