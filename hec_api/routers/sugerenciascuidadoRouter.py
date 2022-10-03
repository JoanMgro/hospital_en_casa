from ..views.sugerenciascuidadoCreateView import SugerenciasViewSet
from rest_framework.routers import DefaultRouter


router_sugerencias = DefaultRouter()
router_sugerencias.register(r'',SugerenciasViewSet, basename='sugerencias')