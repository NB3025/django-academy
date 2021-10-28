from django.contrib import admin

# Register your models here.

from .models import Academy, Teacher

admin.site.register(Academy)
admin.site.register(Teacher)