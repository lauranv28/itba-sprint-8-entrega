from django.contrib import admin
from .models import MarcasDeTarjetas, Tarjeta

# Register your models here.
admin.site.register(Tarjeta)
admin.site.register(MarcasDeTarjetas)