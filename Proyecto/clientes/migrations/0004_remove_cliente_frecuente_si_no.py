# Generated by Django 3.2.7 on 2021-09-23 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_cedula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='frecuente_si_no',
        ),
    ]
