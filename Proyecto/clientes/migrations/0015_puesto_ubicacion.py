# Generated by Django 3.2.7 on 2021-09-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_auto_20210928_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='ubicacion',
            field=models.IntegerField(choices=[(1, 'A1'), (2, 'A2'), (3, 'A3'), (4, 'A4'), (5, 'A5'), (6, 'A6'), (7, 'A7'), (8, 'A8'), (9, 'A9'), (10, 'A10'), (11, 'A11'), (12, 'A12'), (13, 'A13'), (14, 'A14'), (15, 'A15'), (16, 'A16'), (17, 'A17'), (18, 'A18'), (19, 'A19'), (20, 'A20')], null=True, verbose_name='Ubicacion parqueadero'),
        ),
    ]