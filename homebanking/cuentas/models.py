from django.db import models
from clientes.models import Cliente


class TiposDeCuentas(models.Model):
    tipos_de_cuentas_id = models.AutoField(primary_key=True)
    tipo_de_cuenta = models.TextField(
        'Tipo de cuenta', max_length=30, blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo de cuenta'
        db_table = 'tipo_de_cuentas'

"""  def __str__(self):
        return self.tipos_de_cuentas_id """


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.OneToOneField(
        Cliente, default=1, unique=True, on_delete=models.CASCADE)
    balance = models.IntegerField(blank=False, null=False)
    iban = models.TextField()
    # This field type is a guess.
    tipos_de_cuentas_id = models.ForeignKey(TiposDeCuentas, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        db_table = 'cuenta'
