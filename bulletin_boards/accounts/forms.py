import random
from string import hexdigits

from allauth.account.forms import SignupForm
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_managers, mail_admins
from django.core.mail import send_mail


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# class CustomSignupForm(SignupForm):
#     def save(self, request):
#         user = super().save(request)
#         registered_users = Group.objects.get(name='registered users')
#         user.groups.add(registered_users)
#         user.is_active = False
#         code = ''.join(random.sample(hexdigits, 5))
#         RegistrationCode.objects.create(user=request.user, code=code)

# # Чтобы отправить HTML по почте, лучше всего воспользоваться специальным классом EmailMultiAlternatives.
# # Он позволяет одновременно отправить текстовое сообщение и приложить к нему версию с HTML-разметкой.
# class CustomSignupForm(SignupForm):     # форма регистрации по почте
#     def save(self, request):
#         user = super().save(request)
#         all_users = Group.objects.get(name="all_users")
#         user.groups.add(all_users)
#
#         subject = 'Добро пожаловать на наш портал!'
#         text = f'{user.username}, вы успешно зарегистрировались на сайте!'
#         html = (
#             f'<b>{user.username}</b>, вы успешно зарегистрировались на '
#             f'<a href="http://127.0.0.1:8000/">сайте</a>!'
#         )
#         msg = EmailMultiAlternatives(
#             subject=subject, body=text, from_email=None, to=[user.email]
#         )
#         msg.attach_alternative(html, "text/html")
#         msg.send()
#
#         mail_managers(
#             subject='Новый пользователь!',
#             message=f'Пользователь {user.username} зарегистрировался на сайте.'
#         )
#         # mail_admins(
#         #     subject='Новый пользователь!',
#         #     message=f'Пользователь {user.username} зарегистрировался на сайте.'
#         # )
#
#         return user


class CommonSignupForm(SignupForm):
    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        user.is_active = False
        code = ''.join(random.sample(hexdigits, 5))
        user.code = code
        user.save()
        send_mail(
            subject=f'Код активации',
            message=f'Код активации аккаунта: {code}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user





