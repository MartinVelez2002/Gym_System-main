# Generated by Django 4.1.4 on 2023-03-12 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maquinaria', '0004_alter_maquinaria_mantenimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinaria',
            name='Mantenimiento',
            field=models.CharField(blank=True, default=False, max_length=5, null=True),
        ),
    ]