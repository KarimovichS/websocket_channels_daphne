"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from home.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django_asgi_app = get_asgi_application()

ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi()),
    path('ws/new/', NewConsumer.as_asgi())

]

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': URLRouter(ws_patterns)
})
