from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello world")


def get_id(request, id: int):
    return HttpResponse(f"Hello {id}")
rooms = {"rooms":[
        {"id": 1, "name":"room for geeks"},
        {"id": 2, "name": "room for freaks"},
        {"id": 3, "name": "room for creeps"}
    ]}


def page(request):
    context3 = {"rooms":[
        {"id": 1, "name":"room for geeks"},
        {"id": 2, "name": "room for freaks"},
        {"id": 3, "name": "room for creeps"}
    ]}
    return render(request,"base/home.html", context3)
def room(request, pk):
    room = None
    for i in rooms['rooms']:
        if i['id'] == int(pk):
            room = i
    context = {"room": room}
    return render(request,"base/room.html",context)