from django.db import models

from modulos.clientes.models import Cliente
# Create your models here.

class Finanzas (models.Model):

    anio = models.CharField(max_length=4)
    mes = models.CharField(max_length=2)
    mensualidades = models.IntegerField(default=None)
    ingresos = models.IntegerField(default=None)
    gastos = models.IntegerField(default=None)
    ganancias = models.IntegerField(default=None)

