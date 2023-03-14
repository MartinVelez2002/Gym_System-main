from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now
from ecommerse.constantes import Opciones
opciones = Opciones()
GENERO = opciones.genero()
MES = opciones.mes()
# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=GENERO,default=GENERO[0][1], blank=True, null=True)
    cedula = models.CharField(unique=True, max_length=10 ,validators=[RegexValidator(regex='^.{10}$', message='Introduzca una cédula válida')], default='')
    edad = models.IntegerField(default='')
    fecha_de_ingreso = models.DateField(default=now)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)




