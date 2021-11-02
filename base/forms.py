from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Academy, Teacher, Student

class AcademyForm(ModelForm):
    class Meta:
        model = Academy
        fields = '__all__'


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        # exclude = ['academy']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        