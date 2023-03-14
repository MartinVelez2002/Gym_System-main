# Generated by Django 4.1.4 on 2023-01-29 22:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_apellido_alter_cliente_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(default='', max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Introduzca una cédula válida', regex='^.{10}$')]),
        ),
    ]