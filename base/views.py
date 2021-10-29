from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Academy
from .forms import AcademyForm, TeacherForm


def home(request):
    academies = Academy.objects.all()
    context = {'academies':academies}
    return render(request,'base/home.html',context)

# def room(request,pk):
#     room = None
#     for i in rooms:
#         if i['id'] == int(pk):
#             room = i
#     context = {'room':room}
#     return render(request, 'base/room.html', context)

def academy(request,pk):
    academy = Academy.objects.get(id=pk)
    context = {'academy': academy}
    return render(request, 'base/academy.html', context)

def registerAcademy(request):
    form = AcademyForm()

    if request.method =='POST':
        form = AcademyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/academy_form.html',context)
    # return render(request, 'base/academy_register.html',context)

def updateAcademy(request,pk):
    academy = Academy.objects.get(id=pk)
    form = AcademyForm(instance=academy)

    if request.method =='POST':
        form = AcademyForm(request.POST, instance=academy)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render(request, 'base/academy_form.html', context)


def deleteAcademy(request,pk):
    academy=Academy.objects.get(id=pk)
    if request.method == 'POST':
        academy.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':academy})


def registerTeacher(request):
    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    context={'form':form}
    return render(request, 'base/teacher_form.html',context)