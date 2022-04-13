from django.contrib import admin
from appfinal.models import libro, prestamos, socios



# Register your models here.
admin.site.register(socios)

admin.site.register(libro)

admin.site.register(prestamos)
