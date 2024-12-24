from django.db import models
from empleados.models import Empleado  # Relación con el modelo Empleado

class Caja(models.Model):
    TURNO_CHOICES = [
        ('M', 'Mañana'),
        ('T', 'Tarde'),
    ]
    
    # Campos
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='cajas')  # Relación con Empleado
    abierta_caja = models.BooleanField(default=True)  # Estado de la caja (abierta/cerrada)
    fecha_hs_aper_caja = models.DateTimeField(auto_now_add=True)  # Fecha y hora de apertura (automática)
    fecha_hs_cier_caja = models.DateTimeField(blank=True, null=True)  # Fecha y hora de cierre
    monto_inicial_caja = models.DecimalField(max_digits=10, decimal_places=2)  # Monto inicial obligatorio
    total_ingresos_caja = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total ingresos
    total_egresos_caja = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Total egresos
    saldo_caja = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Saldo total
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES, default='M')  # Turno de la caja

    def __str__(self):
        return f"Caja {self.pk} - {self.empleado.nombre_empl}"

    def cerrar_caja(self, fecha_hora_cierre):
        """Cierra la caja calculando el saldo."""
        self.fecha_hs_cier_caja = fecha_hora_cierre
        self.abierta_caja = False
        self.saldo_caja = self.monto_inicial_caja + self.total_ingresos_caja - self.total_egresos_caja
        self.save()
