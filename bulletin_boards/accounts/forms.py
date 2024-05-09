from allauth.account.forms import SignupForm
from django import forms
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



# # Чтобы отправить HTML по почте, лучше всего воспользоваться специальным классом EmailMultiAlternatives.
# # Он позволяет одновременно отправить текстовое сообщение и приложить к нему версию с HTML-разметкой.
class CustomSignupForm(SignupForm):     # форма регистрации
    def save(self, request):
        user = super().save(request)
        all_users = Group.objects.get(name="all_users")
        user.groups.add(all_users)
#
#         # вар_1
#         # # Функция send_mail позволяет отправить письмо указанному получателю в recipient_list.
#         # # В поле subject мы передаём тему письма, а в message — текстовое сообщение.
#         # send_mail(
#         #     subject='Добро пожаловать в наш интернет-магазин!',
#         #     message=f'{user.username}, вы успешно зарегистрировались!',
#         #     from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
#         #     recipient_list=[user.email],
#         # )
#
#         # вар_2
        subject = 'Добро пожаловать на наш новостной портал!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/news">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )
        # mail_admins(
        #     subject='Новый пользователь!',
        #     message=f'Пользователь {user.username} зарегистрировался на сайте.'
        # )

        return user





