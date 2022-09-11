from django.db import models
from cuentas.models import Cuenta

# Create your models here.
class Movimientos(models.Model):
    account_id = models.ForeignKey(Cuenta, models.DO_NOTHING)
    monto = models.IntegerField()
    transaccion = models.TextField()
    fecha = models.TextField()

    class Meta:
        managed = False
        db_table = 'movimientos'
        verbose_name = 'Movimientos'