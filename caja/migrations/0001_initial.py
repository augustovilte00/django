# Generated by Django 5.1.4 on 2024-12-23 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0003_empleado_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abierta_caja', models.BooleanField(default=True)),
                ('fecha_hs_aper_caja', models.DateTimeField(auto_now_add=True)),
                ('fecha_hs_cier_caja', models.DateTimeField(blank=True, null=True)),
                ('monto_inicial_caja', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_ingresos_caja', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total_egresos_caja', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('saldo_caja', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('turno', models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde')], default='M', max_length=1)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cajas', to='empleados.empleado')),
            ],
        ),
    ]
