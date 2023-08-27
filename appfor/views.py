from django.shortcuts import render
from django.http import HttpResponse

from appfor.models import Room


# Create your views here.
def hello(request):
    return HttpResponse("Hello world")


def get_id(request, id: int):
    return HttpResponse(f"Hello {id}")



def page(request):
    rooms = Room.objects.all
    contex = {'rooms': rooms}
    return render(request,"base/home.html", contex)
def room(request, pk):
    room = Room.objects.get(id=pk)
    contex = {'room':room}
    return render(request,"base/room.html",contex)