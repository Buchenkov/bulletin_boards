from django.urls import path

from bulletin_boards.views import ConfirmUser, ProfileView
from . import views
from .views import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
    path('profile/', ProfileView.as_view(), name='profile'),
]