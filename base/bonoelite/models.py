from django.db import models


# Create your models here.
class maestrotrabajadores(models.Model):
    nombre = models.CharField(max_length=40, blank=False, null=True)
    apellido = models.CharField(max_length=40, blank=False, null=True)
    cedula = models.IntegerField()
    ficha = models.CharField(max_length=40, blank=False, null=True)
    nomina = models.CharField(max_length=40, blank=False, null=True)
    tipnom = models.CharField(max_length=40, blank=False, null=True)
    cargo = models.CharField(max_length=120, blank=False, null=True)
    unidad = models.CharField(max_length=120, blank=False, null=True)
    cia = models.CharField(max_length=40, blank=False, null=True)
