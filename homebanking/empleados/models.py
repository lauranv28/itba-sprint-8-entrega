from django.db import models

# Create your models here.
class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField('Nombre', max_length=255, blank=False, null=False)
    employee_surname = models.TextField('Apellido', max_length=255, blank=False, null=False)
    employee_hire_date = models.TextField('Fecha de contratación', blank=False, null=False)
    employee_dni = models.TextField('DNI', max_length=8, db_column='employee_DNI', blank=False, null=False)  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class DireccionEmpleado(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion = models.TextField('Dirección', max_length=255, blank=False, null=False)
    ciudad = models.TextField('Ciudad', max_length=255, blank=False, null=False)
    provincia = models.TextField('Provincia', max_length=255, blank=False, null=False)
    pais = models.TextField('País', max_length=255, blank=False, null=False)
    employee_id = models.ForeignKey(Empleado, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'direcciones'
        verbose_name = 'Dirección del empleado'
        verbose_name_plural = 'Direcciones del empleado'