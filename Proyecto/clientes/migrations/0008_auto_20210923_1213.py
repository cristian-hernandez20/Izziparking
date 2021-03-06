# Generated by Django 3.2.7 on 2021-09-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_rename_precio_estadar_tipo_vehiculo_factura_total_vehiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.FloatField(verbose_name='cedula'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='placa',
            field=models.CharField(max_length=6, verbose_name='placa'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_vehiculo',
            field=models.IntegerField(choices=[(1, 'Camioneta'), (2, 'Motocarro'), (3, 'Automovil'), (4, 'Motocicleta'), (5, 'Bus'), (6, 'Camion')], verbose_name='Tipo de vehiculo'),
        ),
    ]
