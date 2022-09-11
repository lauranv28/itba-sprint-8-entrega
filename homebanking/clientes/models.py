from django.db import models
from django.apps import AppConfig
from login.models import AuthUser
from empleados.models import Sucursal


class Cliente(models.Model):
    # Modelado como la tabla del sprint 6
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField('Nombre', max_length=255)
    customer_surname = models.CharField('Apellido', max_length=255)
    customer_DNI = models.IntegerField('DNI', null=False, blank=False)
    dob = models.DateField('Fecha de nacimiento', null=True)
    branch_id = models.ForeignKey(Sucursal, models.DO_NOTHING)
    username = models.OneToOneField(AuthUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'

    def __str__(self):
        return str(self.username)


class DireccionCliente(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion = models.TextField(
        'Dirección', max_length=255, blank=False, null=False)
    ciudad = models.TextField(
        'Ciudad', max_length=255, blank=False, null=False)
    provincia = models.TextField(
        'Provincia', max_length=255, blank=False, null=False)
    pais = models.TextField('País', max_length=255, blank=False, null=False)
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Dirección del cliente'
        verbose_name_plural = 'Direcciones del cliente'
        db_table = 'direccion_cliente'


class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True)
    tipos_de_clientes = models.TextField(
        'Tipo de cliente', blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo de cliente'
        db_table = 'tipo_cliente'
