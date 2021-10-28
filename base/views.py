from django.shortcuts import render
from django.http import HttpResponse
from .models import Academy

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Hello django!'}
]

def home(request):
    academies = Academy.objects.all()
    context = {'academies':academies}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)

def registerAcademy(request):
    context = {}
    return render(request, 'base/academy_register.html',context)
