from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register-academy/', views.registerAcademy, name="register-academy"),
    
    path('register-teacher/', views.registerTeacher, name="register-teacher"),
    
    path('academy/<str:pk>/', views.academy, name='academy')
    
    # path('room/<str:pk>/', views.room, name='room')
]