from django import forms
from django.core.exceptions import ValidationError

from .models import *


class ArticleForm(forms.ModelForm):
    # text = forms.CharField(min_length=20)
    class Meta:
        model = Article
        # fields = '__all__'  # все пункты
        fields = [
            'author',
            'category',
            'title',
            'text',
        ]
        # print(fields)

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError(
                "Text: Описание не может быть менее 20 символов."
            )

        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'  # все пункты
        fields = ['text']
        # labels = {
        #     'text': 'Введите текст отклика'
        # }
        # widgets = {
        #     'text': forms.Textarea(attrs={'class': 'form-text', 'cols': 200, 'rows': 2})
        # }
