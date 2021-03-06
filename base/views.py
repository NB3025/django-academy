from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Academy, Teacher, Student
from .forms import AcademyForm, TeacherForm, StudentForm


def home(request):
    academies = Academy.objects.all()
    context = {'academies':academies}
    return render(request,'base/home.html',context)


def academy(request,pk):
    academy = Academy.objects.get(id=pk)
    teachers = Teacher.objects.filter(academy=academy.id)
    students = Student.objects.filter(academy=academy.id)

    context = {'academy': academy, 'teachers':teachers, 'students':students}
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


def updateTeacher(request,pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)

    if request.method =='POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/teacher_form.html', context)


def deleteTeacher(request,pk):
    teacher=Teacher.objects.get(id=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':teacher})


def registerStudent(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/student_form.html', context)


def updateStudent(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method =='POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/student_form.html', context)


def deleteStudent(request,pk):
    student=Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':student})