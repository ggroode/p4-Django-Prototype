# chat/routing.py
from django.conf.urls import re_path, url

from . import consumers

websocket_urlpatterns = [
   re_path(r'ws/setup$', consumers.SetupConsumer.as_asgi()),
   re_path(r'ws/play$', consumers.PlayConsumer.as_asgi()),
]
