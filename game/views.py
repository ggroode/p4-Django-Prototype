# chat/views.py
from django.shortcuts import render
import json


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
    players = json.loads(request.GET.get('players', "[\"Gavin\",\"Yingyan\"]")) #TODO: change default value of off testing one
    updateSpeed = request.GET.get('updateSpeed','normal')
    time = request.GET.get('time',20)
    prompt = request.GET.get('prompt','true')
    return render(request, 'game/play.html',{'players':json.dumps(players),'playersList':players,'updateSpeed':updateSpeed,'roundTime':time,'prompt':prompt})

def write(request):
    name = request.GET.get('name','Gavin') #TODO: change default value of off testing one
    return render(request, 'game/write.html',{'name':name})
