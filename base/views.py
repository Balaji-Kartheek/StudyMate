from django.shortcuts import render
from .models import Room


# rooms = [
#     {'id': 1, 'name': "Let's build Python Projects"},
#     {'id': 2, 'name': 'Lets build Django Projects'},
#     {'id': 3, 'name': 'Lets build React Projects'},
# ]

# Create your views here.
from django.http import HttpResponse

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request,'base/room.html', context)