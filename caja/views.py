from rest_framework import viewsets
from .models import Caja
from .serializers import CajaSerializer

class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer
