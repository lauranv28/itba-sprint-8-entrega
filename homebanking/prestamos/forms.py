from enum import unique
from django import forms
from clientes.models import Cliente, TipoCliente

class FormularioPrestamo(forms.Form):
    name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    dni = forms.IntegerField(label='DNI', required=True)
    email = forms.EmailField(label='Email', required=True)
    monto = forms.IntegerField(label='Monto solicitado', required=True)
    tipo_prestamo = forms.CharField(label='Tipo de préstamo', required=True)
    fecha_inicio = forms.DateField(label='Fecha de inicio', required=True)
