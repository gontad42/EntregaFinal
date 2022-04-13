from django.db import models

# Create your models here.

class socios(models.Model):
    
    nombre = models.CharField(max_length= 10)
    apellido = models.CharField(max_length= 10)
    nacimiento = models.DateField()
    email = models.EmailField()

class libro(models.Model):

    titulo = models.CharField(max_length= 20)
    autor = models.CharField(max_length= 40)
    genero = models.CharField(max_length= 20)
    editorial = models.CharField(max_length= 50)
    año = models.DateField()

class prestamos(models.Model):

    apellido = models.CharField(max_length= 40)
    nombre =  models.CharField(max_length= 40)
    titulo = models.CharField(max_length= 40)
    fecha_prest = models.DateField()
    


