from rest_framework import serializers
from .models import Empleado
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = (
            'id', 'dni_empl', 'nombre_empl', 'apellido_empl', 
            'domicilio_empl', 'telefono_empl', 'correo_empl', 
            'admin', 'is_active', 'password'
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, empleado):
        token = super().get_token(empleado)
        # Agregar campos personalizados al token
        token['nombre'] = empleado.nombre_empl
        token['admin'] = empleado.admin
        return token

    def validate(self, attrs):
        correo = attrs.get("username")
        password = attrs.get("password")
        print(f"{correo} {password}")
        try:
            empleado = Empleado.objects.get(correo_empl=correo)
        except Empleado.DoesNotExist:
            raise AuthenticationFailed("Credenciales inválidas EMPLEADO NO EXISTE.")

        if not check_password(password, empleado.password):
            raise AuthenticationFailed("Credenciales inválidas MAL PASSWORD.")

        access_token = self.get_token(empleado).access_token  # Solo el access_token
        return {
            "access": str(access_token),
            "idempleado":empleado.id
        }  # Retorna solo el access token