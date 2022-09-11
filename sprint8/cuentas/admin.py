from django.contrib import admin
from .models import Cuenta, TiposDeCuentas

# Register your models here.
admin.site.register(Cuenta)
admin.site.register(TiposDeCuentas)