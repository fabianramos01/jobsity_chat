from django.urls import path, include
from django.contrib.auth.views import logout_then_login

from chat_app.utils import user_not_authenticated
from .views import register, login_user

urlpatterns = [
    path('', user_not_authenticated(login_user), name='login'),
    path('register', user_not_authenticated(register), name='register'),
    path('logout', logout_then_login, name='logout'),
]
