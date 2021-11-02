from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # path('register-academy/', views.registerAcademy, name="register-academy"),
    path('register-academy/', views.registerAcademy, name="register-academy"),
    path('update-academy/<str:pk>/', views.updateAcademy, name="update-academy"),
    path('delete-academy/<str:pk>/', views.deleteAcademy, name="delete-academy"),
    
    path('register-teacher/', views.registerTeacher, name="register-teacher"),
    
    path('register-student/', views.registerStudent, name="register-student"),

    path('academy/<str:pk>/', views.academy, name='academy')
    
    # path('room/<str:pk>/', views.room, name='room')
]