# Generated by Django 3.2.7 on 2021-10-06 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0017_auto_20211005_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='dueño_vehiculo',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='placa_vehiculo',
        ),
        migrations.RemoveField(
            model_name='parqueadero',
            name='placa_vehiculo',
        ),
        migrations.DeleteModel(
            name='Puesto',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='dueño_vehiculo',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='Parqueadero',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]