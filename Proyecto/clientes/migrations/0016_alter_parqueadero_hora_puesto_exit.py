# Generated by Django 3.2.7 on 2021-10-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0015_puesto_ubicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parqueadero',
            name='hora_puesto_exit',
            field=models.TimeField(verbose_name='Hora de salida'),
        ),
    ]
