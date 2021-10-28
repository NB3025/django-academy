from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('register-academy/', views.registerAcademy, name="register-academy"),
    
    path('room/<str:pk>/', views.room, name='room')
]