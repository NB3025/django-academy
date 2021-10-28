from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Hello django!'}
]

def index(request):
    context = {'rooms':rooms}
    return render(request,'home.html',context)