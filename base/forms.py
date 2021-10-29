from django.forms import ModelForm, fields
from .models import Academy, Teacher

class AcademyForm(ModelForm):
    class Meta:
        model = Academy
        fields = '__all__'


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        # exclude = ['academy']