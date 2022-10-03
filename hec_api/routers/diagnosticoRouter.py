from ..views.diagnosticoCreateView import DiagnosticoViewSet
from rest_framework.routers import DefaultRouter


router_diagnostico = DefaultRouter()
router_diagnostico.register(r'',DiagnosticoViewSet, basename='diagnostico')