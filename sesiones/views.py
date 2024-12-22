from rest_framework.viewsets import ModelViewSet
from .models import Sesion
from .serializers import SesionSerializer

class SesionViewSet(ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer
