from django.db import models
from empleados.models import Empleado  # Importar el modelo Empleado

class Sesion(models.Model):
    id_logueo = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="sesiones")
    fecha_hora_inicio = models.DateTimeField(auto_now_add=True)
    fecha_hora_fin = models.DateTimeField(null=True, blank=True)
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)  # Puedes cifrarla usando un método seguro
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Sesión de {self.nombre_usuario} ({self.id_empleado})"
