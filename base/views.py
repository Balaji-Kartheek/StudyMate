from django.shortcuts import render


rooms = [
    {'id': 1, 'name': "Let's build Python Projects"},
    {'id': 2, 'name': 'Lets build Django Projects'},
    {'id': 3, 'name': 'Lets build React Projects'},
]

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'home.html', {'rooms': rooms})

def room(request):
    return render(request,'room.html')