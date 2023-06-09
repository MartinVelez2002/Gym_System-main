# Generated by Django 4.1.4 on 2023-03-05 21:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0007_alter_cliente_cedula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensualidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, default='', max_digits=9, verbose_name='Pago')),
                ('fecha_inicio', models.DateField(default=django.utils.timezone.now)),
                ('fecha_finalizacion', models.DateField(default=None)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Mensualidad',
                'verbose_name_plural': 'Mensualidades',
                'ordering': ('cliente',),
            },
        ),
    ]
