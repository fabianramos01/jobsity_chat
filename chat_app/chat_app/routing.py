from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from apps.chat.routing import websocket_url_patterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(websocket_url_patterns))
})
