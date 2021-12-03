from django.db import models
from datetime import date
from django.db.models.enums import Choices
from django.db.models.query_utils import select_related_descend

from django.utils.translation import override
# Create your models here.

ubicaci = [(1,"A1"),
               (2,"A2"),
               (3,"A3"),
               (4,"A4"),
               (5,"A5"),
               (6,"A6"),
               (7,"A7"),
               (8,"A8"),
               (9,"A9"),
               (10,"A10"),
               (11,"A11"),
               (12,"A12"),
               (13,"A13"),
               (14,"A14"),
               (15,"A15"),
               (16,"A16"),
               (17,"A17"),
               (18,"A18"),
               (19,"A19"),
               (20,"A20"),
               ]

class Puesto(models.Model):
    titulo=models.CharField(unique=False, null=True,max_length=50)
    contenido=models.CharField(unique=False, null=True,max_length=500)
    imagen=models.ImageField(unique=False, null=True,upload_to='puestos')
    created=models.DateTimeField(unique=False, null=True,auto_now_add=True)
    updated=models.DateTimeField(unique=False, null=True,auto_now_add=True)
    ubicacion=models.IntegerField(unique=False, null=True, blank = False,choices=ubicaci,verbose_name="Ubicacion")
    ocupado = models.BooleanField(unique=False, null=True)
    
    class Meta:

        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"

    def __str__(self):
        return self.titulo