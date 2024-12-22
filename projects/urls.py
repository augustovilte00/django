from rest_framework import routers
from .api import ProjectViewSet
from empleados.views import EmpleadoViewSet  # Importa el ViewSet de empleados
from sesiones.views import SesionViewSet 

router = routers.DefaultRouter()

router.register('projects', ProjectViewSet, 'projects')
router.register('empleados', EmpleadoViewSet, 'empleados')
router.register('sesiones', SesionViewSet, 'sesiones')

urlpatterns = router.urls

