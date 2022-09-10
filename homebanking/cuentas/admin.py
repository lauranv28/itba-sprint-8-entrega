from django.contrib import admin
from .models import Cuenta, TiposDeCuentas

admin.site.register(Cuenta)
admin.site.register(TiposDeCuentas)