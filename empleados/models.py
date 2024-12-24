from django.db import models
from django.contrib.auth.hashers import make_password

class Empleado(models.Model):
    dni_empl = models.CharField(max_length=20, unique=True)
    nombre_empl = models.CharField(max_length=50)
    apellido_empl = models.CharField(max_length=50)
    domicilio_empl = models.CharField(max_length=100)
    telefono_empl = models.CharField(max_length=20, blank=True, null=True)
    correo_empl = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Cifrada con Django
    admin = models.BooleanField(default=False)  # False = Usuario normal, True = Admin
    is_active = models.BooleanField(default=True)  # Indica si la cuenta está activa

    def str(self):
        return f"{self.nombre_empl} {self.apellido_empl}"

    def save(self, *args, **kwargs):
    # Cifrado de contraseña si no está cifrada
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
