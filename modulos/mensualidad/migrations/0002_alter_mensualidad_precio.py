# Generated by Django 4.1.5 on 2023-03-14 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensualidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensualidad',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=25, max_digits=9, verbose_name='Pago'),
        ),
    ]