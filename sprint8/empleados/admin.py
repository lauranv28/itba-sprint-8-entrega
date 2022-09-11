from django.contrib import admin
from .models import Sucursal, Empleado, DireccionEmpleado

# Register your models here.
admin.site.register(Sucursal)
admin.site.register(Empleado)
admin.site.register(DireccionEmpleado)