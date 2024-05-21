"""
Django settings for bulletin_boards project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9cjys4hdgci403xd(5qh3#v!ia7!76vk=%i35&$8jj0ns7&+)b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # для - DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sites',

    'bulletin_boards',
    'accounts',
    # 'subscriptions',

    'ckeditor',
    'ckeditor_uploader',
    # 'ckeditor_skins',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',  # отвечает за выход через Yandex
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'bulletin_boards.urls'

# ROOT_URLCONF = 'project.urls'

MEDIA_ROOT = BASE_DIR / 'uploads'   # это физический каталог, в котором хранятся файлы
MEDIA_URL = '/uploads/'   # URL, который мы используем для отправки загруженных файлов клиенту (mysite.com/media/uploads/2020/06/11/04.jpg)

STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # ->  python manage.py collectstatic
STATICFILES_DIRS = [BASE_DIR / 'static', ]   # com
STATIC_DIR = os.path.join(BASE_DIR, 'static')   # com

CKEDITOR_UPLOAD_PATH = "uploads/"   #  указывает каталог, в котором хранятся загруженные файлы, внутри MEDIA_ROOT каталога (media/uploads)
# CKEDITOR_IMAGE_BACKEND = "pillow"
# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# #
# CKEDITOR_CONFIGS = {
#     'default':
#         {
#             'toolbar': 'full',
#             'width': 'auto',
#             'extraPlugins': ','.join([
#                 'codesnippet',
#             ]),
#         },
# }

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # os.path.join(BASE_DIR, 'templates')
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'bulletin_boards.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5    # Ограничение попыток входа в систему
LOGIN_URL = 'account_login'             # '/login/'
LOGIN_REDIRECT_URL = 'profile'          # '/'
LOGOUT_REDIRECT_URL = 'account_login'   # '/'

# # Первые два параметра указывают на то, что поле email является обязательным и уникальным. Третий, наоборот, — говорит,
# # что username необязательный. Следующий параметр указывает, что аутентификация будет происходить посредством
# # электронной почты. Напоследок мы указываем, что верификация почты отсутствует.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # 'none'
# # mandatory — не пускать пользователя на сайт до момента подтверждения почты;
# # optional — сообщение о подтверждении почты будет отправлено, но пользователь может залогиниться на сайте без подтверждения почты.
ACCOUNT_FORMS = {'signup': 'accounts.forms.CommonSignupForm'}
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # позволит избежать дополнительного входа и активирует аккаунт сразу,
# # как только мы перейдём по ссылке.
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7  # хранит количество дней, когда доступна ссылка на подтверждение регистрации
AUTH_USER_MODEL = 'bulletin_boards.User'    # разобраться

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # который просто напечатает его в консоли.
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "igorchan"
EMAIL_HOST_PASSWORD = "jwitospiqdwbrxpf"
# EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = ['Bulletin boards']
DEFAULT_FROM_EMAIL = "igorchan@yandex.ru"

SERVER_EMAIL = "igorchan@yandex.ru"
MANAGERS = [
    ('igor', 'igorchan@mail.ru'),
]

ADMINS = (
    ('igor', 'igorchan@yandex.ru'),  # текст в account/forms.py
)


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',
            {'name': 'yourcustomtools', 'items': [
                'Preview',
                'Maximize',
                'Youtube',
            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'youtube',
        ]),
    }
}

# Пример конфигурации ckeditor
# CKEDITOR_CONFIGS = {
#     'default': {
#         # 'skin': 'moono',
#         # 'skin': 'office2013',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         'toolbar_YourCustomToolbarConfig': [
#             {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#             {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#             {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
#             {'name': 'forms',
#              'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
#                        'HiddenField']},
#             '/',
#             {'name': 'basicstyles',
#              'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#             {'name': 'paragraph',
#              'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                        'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                        'Language']},
#             {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#             {'name': 'insert',
#              'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#             '/',
#             {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
#             {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#             {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#             {'name': 'about', 'items': ['About']},
#             '/',  # put this to force next toolbar on new line
#             {'name': 'yourcustomtools', 'items': [
#                 # put the name of your editor.ui.addButton here
#                 'Preview',
#                 'Maximize',
#                 'Youtube',
#             ]},
#         ],
#         'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#         # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
#         # 'height': 291,
#         # 'width': '100%',
#         # 'filebrowserWindowHeight': 725,
#         # 'filebrowserWindowWidth': 940,
#         # 'toolbarCanCollapse': True,
#         # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#         'tabSpaces': 4,
#         'extraPlugins': ','.join([
#             'uploadimage', # the upload image feature
#             # your extra plugins here
#             'div',
#             'autolink',
#             'autoembed',
#             'embedsemantic',
#             'autogrow',
#             # 'devtools',
#             'widget',
#             'lineutils',
#             'clipboard',
#             'dialog',
#             'dialogui',
#             'elementspath',
#             # 'youtube',
#         ]),
#     }
# }


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # средства форматирования
    'formatters': {
        'format_debug': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },

        'format_warning_mail': {
            'format': '{asctime} {levelname} {message} {pathname} ',
            'style': '{',
        },

        'format_general_security_info': {
            'format': '{asctime} {levelname} {message} {module} ',
            'style': '{',
        },

        'format_error_critical': {
            'format': '{asctime} {levelname} {message} {pathname} {exc_info}',
            'style': '{',
        },
    },
    # обработчики
    'handlers': {
        'console_debug': {
            'level': 'INFO',  # 'DEBUG'
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_debug',
        },

        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_warning_mail',
        },

        'console_gen_sec_info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'format_general_security_info',
            'filename': 'general.log',
        },

        'console_error_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'format_error_critical',
        },

        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'format_error_critical',
            'filename': 'errors.log',
        },

        'security_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'format_general_security_info',
            'filename': 'security.log',
        },

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'format_warning_mail',
        },
    },
    # фильтры
    'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
    },
    # регистраторы
    'loggers': {
        'django': {
            'handlers': ['console_debug', 'console_warning', 'console_gen_sec_info', 'console_error_critical'],
            'level': 'INFO',  # 'DEBUG'
            'propagate': True,
        },

        'django.request': {
            # Этот логгер обрабатывает все сообщения вызванные HTTP-запросами и вызывает исключения для определенных кодов состояния. Все коды ошибок HTTP 5xx будут вызывать сообщения об ERROR. Аналогичным образом, коды HTTP 4xx будут отображаться в виде WARNING
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.server': {
            # Когда сервер запускается с помощью команды runserver, он будет регистрировать сообщения, связанные с обработкой этих запросов
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.db.backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.security': {
            'handlers': ['security_file'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
