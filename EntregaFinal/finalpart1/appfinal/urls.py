
from django import views
from django.contrib import admin
from django.urls import path
from .views import socio , Libro , Prestamo, registroformulario
from .models import *
from appfinal import views



urlpatterns = [
    
    path('socios' , views.socio , name="socio"), 
    path('libros', views.Libro, name= "libros"),
    path('prestamos', views.Prestamo, name= "Prestamos"),
    path('', views.Inicio, name= "Inicio"),
    path('login', views.registroformulario, name="login"),
    path('prestacion', views.prestamoformulario, name="prestacion"),
]

