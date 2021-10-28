from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register-academy/', views.registerAcademy, name="register-academy"),
    
    path('room/<str:pk>/', views.room, name='room')
]