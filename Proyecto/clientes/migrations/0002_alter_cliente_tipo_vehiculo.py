# Generated by Django 3.2.7 on 2021-09-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_vehiculo',
            field=models.IntegerField(choices=[(1, 'Camioneta'), (2, 'Motocarro'), (3, 'Automovil'), (4, 'Motocicleta'), (5, 'Bus'), (6, 'Camion')]),
        ),
    ]
