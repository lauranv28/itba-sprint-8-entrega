# Generated by Django 4.1 on 2022-09-11 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_sucursal'),
        ('clientes', '0004_merge_20220911_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='branch_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='empleados.sucursal'),
        ),
        migrations.AlterModelTable(
            name='cliente',
            table='cliente',
        ),
    ]
