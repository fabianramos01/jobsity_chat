from django.urls import path

from apps.chat.consumer import ChatConsumer

websocket_url_patterns = [
    path('chat/<str:room>/', ChatConsumer.as_asgi())
]