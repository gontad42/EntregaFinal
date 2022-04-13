import email
import re
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from django.template import Template , context
from django.http import HttpRequest, HttpResponse
from appfinal.models import socios , libro , prestamos
from appfinal import views
from appfinal.forms import RegistroFormulario
from appfinal.forms import PrestamoFormulario

# Create your views here.

def Inicio(request): 

    

    return render(request,'inicio.html')


def socio(request): 
    template= loader.get_template('socios.html')
    socios1 = socios.objects.all()
    context = {"socio": socios1}
    return HttpResponse(template.render(context,request))




def Libro(request): 
    template= loader.get_template('libros.html')
    Libro1 = libro.objects.all()
    context = {"socio": Libro1}
    return HttpResponse(template.render(context,request))




def Prestamo(request): 
    template= loader.get_template('prestamos.html')
    Prestamo1 = prestamos.objects.all()
    context = {"prestamos": Prestamo1}
    return HttpResponse(template.render(context,request))


def registroformulario(request):

    if request.method == "POST":

        formulario= RegistroFormulario(request.POST)

        print(formulario)

        if formulario.is_valid:
            info = formulario.cleaned_data

            socio1  = socios (nombre=info['nombre'], apellido=info ['apellido'], nacimiento=info['nacimiento'], email=info['email'])
            
            socio1.save()
            return render(request, "inicio.html")
    else:
        formulario=RegistroFormulario()
        

        return render(request, 'registroformulario.html' , {"formulario": formulario})


def prestamoformulario(request):

    if request.method == "POST":

        formulario2= PrestamoFormulario(request.POST)

        print(formulario2)

        if formulario2.is_valid:
            info = formulario2.cleaned_data

            socio1  = prestamos (nombre=info['nombre'], apellido=info ['apellido'], titulo=info['titulo'], fecha_prest=info['fecha_prest'])
            
            socio1.save()
            return render(request, "libros.html")
    else:
        formulario2=PrestamoFormulario()
        

        return render(request, 'prestamoformulario.html' , {"formulario2": formulario2})








    
        
        

