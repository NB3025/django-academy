from django.forms import ModelForm, fields
from .models import Academy

class AcademyForm(ModelForm):
    class Meta:
        model = Academy
        fields = '__all__'