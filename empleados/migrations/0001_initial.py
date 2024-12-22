# Generated by Django 5.1.4 on 2024-12-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_empl', models.CharField(max_length=20, unique=True)),
                ('nombre_empl', models.CharField(max_length=50)),
                ('apellido_empl', models.CharField(max_length=50)),
                ('domicilio_empl', models.CharField(max_length=100)),
                ('telefono_empl', models.CharField(blank=True, max_length=20, null=True)),
                ('correo_empl', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]