# Generated by Django 4.1 on 2022-09-11 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_alter_sucursal_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='branch_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
