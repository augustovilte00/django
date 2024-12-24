from rest_framework import serializers
from .models import Caja

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = '__all__'
        read_only_fields = ('fecha_hs_aper_caja', 'saldo_caja', 'abierta_caja')
