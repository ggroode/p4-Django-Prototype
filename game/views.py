# chat/views.py
from django.shortcuts import render


# def room(request, room_name):
#     return render(request, 'game/room.html', {
#         'room_name': room_name
#     })

def start(request):
    return render(request, 'game/start.html')

def join(request):
    return render(request, 'game/join.html')

def settings(request):
    return render(request, 'game/settings.html')

def play(request):
    return render(request, 'game/play.html')

def write(request):
    return render(request, 'game/write.html')
