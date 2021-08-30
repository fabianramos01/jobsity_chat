from django.urls import path, include
from django.contrib.auth.decorators import login_required

from apps.chat.views import home

urlpatterns = [
    path('<str:room_name>/', login_required(home), name='home')
]
