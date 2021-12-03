from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import Puesto
# Register your models here.


@admin.register(Puesto)
class puestosAdmin(admin.ModelAdmin):
    readonly_fields=()
