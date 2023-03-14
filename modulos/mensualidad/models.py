from django.db import models
from django.utils import timezone
from modulos.clientes.models import *
from django.utils.timezone import now
# Create your models here.



class Mensualidad(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    precio = models.DecimalField(default='', max_digits=9, decimal_places=2, verbose_name='Pago')
    fecha_inicio = models.DateField(default=now)
    fecha_finalizacion= models.DateField(default=None)

    def __str__(self):
        return "{}".format(self.cliente)

    class Meta:
        verbose_name = "Mensualidad"
        verbose_name_plural = "Mensualidades"
        ordering = ('cliente',)