# Generated by Django 4.1 on 2022-09-12 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_alter_cliente_branch_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='branch_id',
        ),
    ]
