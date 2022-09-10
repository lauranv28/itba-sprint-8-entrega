from django.db import models
from clientes.models import Cliente

class MarcasDeTarjetas(models.Model):
    marcas_tarjeta_id = models.AutoField(primary_key=True)
    marca_tarjeta = models.TextField('Marca tarjeta', max_length=70, blank=False, null=False)

    class Meta:
        verbose_name = 'Marca de tarjeta'

    def __str__(self):
        return self.marcas_tarjeta_id


class Tarjeta(models.Model):
    numero = models.TextField(primary_key=True)
    cvv = models.TextField('CVV', db_column='CVV', blank=False, null=False)  # Field name made lowercase.
    fecha_de_otorgamiento = models.TextField('Fecha de otrogamiento', blank=False, null=False)
    fecha_de_vencimiento = models.TextField('Fecha de vencimiento', blank=False, null=False)
    tipo_tarjeta = models.TextField('Tipo de tarjeta', blank=False, null=False)
    marcas_tarjeta = models.ForeignKey(MarcasDeTarjetas, models.DO_NOTHING)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Tarjeta'
        verbose_name_plural = 'Tarjetas'
