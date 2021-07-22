# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('settings',views.settings, name='settings'),
    path('play',views.play,name='play'),
    path('join',views.join,name='join'),
    path('write',views.write,name='write'),
    # path('<str:room_name>/', views.room, name='room'),

]
