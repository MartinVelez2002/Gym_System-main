# Generated by Django 4.1.4 on 2023-03-06 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finanzas',
            name='anio',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='finanzas',
            name='mes',
            field=models.CharField(max_length=2),
        ),
    ]