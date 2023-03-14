from django.db import models
from django.utils.timezone import now

from ecommerse.constantes import Opciones

opciones = Opciones()
MASA = opciones.masa()


class Instrumento(models.Model):
    descripcion = models.CharField(verbose_name='Descripcion', max_length=100)
    peso = models.CharField(verbose_name='peso', max_length=100)
    precio_instrumento = models.IntegerField(default=0)
    fecha_compra_instrumento = models.DateField(default=now)
    unidades = models.CharField(max_length=18, choices=MASA, default=MASA[0][1], blank=True, null=True)
    cantidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.descripcion
