from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, empleado):
        token = super().get_token(empleado)
        token['nombre'] = empleado.nombre_empl
        token['admin'] = empleado.admin
        return token

    def validate(self, attrs):
        print('algooaosodas')
        correo = attrs.get("username")
        password = attrs.get("password")
        print(f"{correo} {password}")
        try:
            empleado = Empleado.objects.get(correo_empl=correo)
            print(empleado.password)
        except Empleado.DoesNotExist:
            raise AuthenticationFailed("No existe un empleado con este correo.")

        if not check_password(password, empleado.password):
            raise AuthenticationFailed("Contraseña incorrecta.")
        
        data = super().validate(attrs)
        refresh = self.get_token(empleado)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        return data
