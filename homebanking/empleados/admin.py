from django.contrib import admin
from empleados.models import DireccionEmpleado, Empleado

# Register your models here.
admin.site.register(Empleado)
admin.site.register(DireccionEmpleado)