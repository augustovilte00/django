# Generated by Django 5.1.4 on 2024-12-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='empleado',
            name='password',
            field=models.CharField(default=123, max_length=128),
            preserve_default=False,
        ),
    ]
