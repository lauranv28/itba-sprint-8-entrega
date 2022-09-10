from django.db import models
from clientes.models import Cliente

class TiposDeCuentas(models.Model):
    tipos_de_cuentas_id = models.AutoField(primary_key=True)
    tipo_de_cuenta = models.TextField('Tipo de cuenta', max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo de cuenta'

    def __str__(self):
        return self.tipos_de_cuentas_id


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)
    balance = models.IntegerField(blank=False, null=False)
    iban = models.TextField()
    tipos_de_cuentas_id = models.ForeignKey(TiposDeCuentas, models.DO_NOTHING)  # This field type is a guess.

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
