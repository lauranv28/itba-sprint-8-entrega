from django.db import models
from clientes.models import Cliente

class Prestamos(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField('Tipo de préstamo', max_length=30, blank=False, null=False)
    loan_date = models.TextField('Fecha', blank=False, null=False)
    loan_total = models.IntegerField('Total', blank=False, null=False)
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING)

    class Meta:
        verbose_name = 'Préstamo'
        verbose_name_plural = 'Préstamos'