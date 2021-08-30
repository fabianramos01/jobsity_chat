import json

from django.shortcuts import render, redirect
from django.urls import reverse

from apps.chat.models import Room, Message

def home(request, room_name):
    room = Room.objects.filter(name=room_name)
    if not room.exists():
        return redirect(reverse('home' , kwargs={'room_name': 'jobsity'}))
    room_list = Room.objects.all()
    message_list = Message.objects.filter(room=room[0]).order_by('timestamp')[:50]
    return render(request, 'home.html', {
        'room_name': room_name,
        'rooms': room_list,
        'messages': message_list
    })
