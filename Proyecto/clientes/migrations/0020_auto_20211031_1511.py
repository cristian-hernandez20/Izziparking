# Generated by Django 3.2.7 on 2021-10-31 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0019_cliente_factura_parqueadero_puesto_reserva_vehiculo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Puesto',
        ),
        migrations.AlterField(
            model_name='parqueadero',
            name='hora_puesto_exit',
            field=models.TimeField(null=True, verbose_name='Hora de salida'),
        ),
    ]
