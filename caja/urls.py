from rest_framework.routers import DefaultRouter
from caja.views import CajaViewSet

router = DefaultRouter()
router.register(r'cajas', CajaViewSet, basename='cajas')

urlpatterns = router.urls