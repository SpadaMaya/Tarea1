# Generated by Django 4.2.2 on 2023-06-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Sin nombre', max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(default='Sin descripción', verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, default='Sin precio', max_digits=8, verbose_name='Precio')),
                ('fecha_registro', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('estatus', models.BooleanField(default=True, verbose_name='Estatus')),
            ],
        ),
    ]
