# Generated by Django 4.1 on 2022-09-11 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarcasDeTarjetas',
            fields=[
                ('marcas_tarjeta_id', models.AutoField(primary_key=True, serialize=False)),
                ('marca_tarjeta', models.TextField(max_length=70, verbose_name='Marca tarjeta')),
            ],
            options={
                'verbose_name': 'Marca de tarjeta',
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('numero', models.TextField(primary_key=True, serialize=False)),
                ('cvv', models.TextField(db_column='CVV', verbose_name='CVV')),
                ('fecha_de_otorgamiento', models.TextField(verbose_name='Fecha de otrogamiento')),
                ('fecha_de_vencimiento', models.TextField(verbose_name='Fecha de vencimiento')),
                ('tipo_tarjeta', models.TextField(verbose_name='Tipo de tarjeta')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
                ('marcas_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tarjetas.marcasdetarjetas')),
            ],
            options={
                'verbose_name': 'Tarjeta',
                'verbose_name_plural': 'Tarjetas',
            },
        ),
    ]
