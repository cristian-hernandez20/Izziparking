# Generated by Django 3.2.7 on 2021-10-31 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puestos', '0003_auto_20211031_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='puesto',
            name='ocupado',
        ),
        migrations.RemoveField(
            model_name='puesto',
            name='ubicacion',
        ),
    ]