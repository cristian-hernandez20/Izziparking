# Generated by Django 3.2.7 on 2021-11-01 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puestos', '0008_alter_puesto_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puesto',
            name='ocupado',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='puesto',
            name='ubicacion',
            field=models.IntegerField(choices=[(1, 'A1'), (2, 'A2'), (3, 'A3'), (4, 'A4'), (5, 'A5'), (6, 'A6'), (7, 'A7'), (8, 'A8'), (9, 'A9'), (10, 'A10'), (11, 'A11'), (12, 'A12'), (13, 'A13'), (14, 'A14'), (15, 'A15'), (16, 'A16'), (17, 'A17'), (18, 'A18'), (19, 'A19'), (20, 'A20')], null=True),
        ),
    ]
