from rest_framework import routers
from .api import ProjectViewSet
from empleados.views import EmpleadoViewSet  # Importa el ViewSet de empleados
from sesiones.views import SesionViewSet 
from caja.views import CajaViewSet 

router = routers.DefaultRouter()

router.register('projects', ProjectViewSet, 'projects')
router.register('empleados', EmpleadoViewSet, 'empleados')
router.register('sesiones', SesionViewSet, 'sesiones')
router.register('caja', CajaViewSet, 'caja')

urlpatterns = router.urls

