from django.db import models
from django.utils.timezone import now


class Maquinaria(models.Model):
    Descripcion = models.CharField(max_length=130, unique=True)
    Cantidad = models.IntegerField(default='')
    precio_maquinaria = models.IntegerField(default=0)
    fecha_compra_maquinaria = models.DateField(default=now)
    Mantenimiento = models.BooleanField(default=False)


    def __str__(self):
        return "{}".format(self.Descripcion)

    class Meta:
        ordering = ('Descripcion',)
