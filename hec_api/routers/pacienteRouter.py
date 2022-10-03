from ..views.pacienteCreateview import PacienteViewSet
from rest_framework.routers import DefaultRouter


router_paciente = DefaultRouter()
router_paciente.register(r'',PacienteViewSet, basename='paciente')