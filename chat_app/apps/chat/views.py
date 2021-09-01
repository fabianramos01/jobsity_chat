import json

from django.shortcuts import render, redirect
from django.urls import reverse

from apps.chat.models import Room, Message
from apps.chat.forms import RoomForm

def home(request, room_name):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user
            room.save()
            room_name = room.name
    room = Room.objects.filter(name=room_name)
    if not room.exists():
        return redirect(reverse('home' , kwargs={'room_name': 'jobsity'}))
    room_list = Room.objects.all()
    message_list = Message.objects.filter(room=room[0]).order_by('timestamp')[:50]
    return render(request, 'home.html', {
        'room_name': room_name,
        'rooms': room_list,
        'messages': message_list,
        'form': form
    })


