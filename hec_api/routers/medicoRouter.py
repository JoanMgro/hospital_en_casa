from rest_framework.routers import DefaultRouter
from ..views.medicoCreateView import MedicoApiViewSet

router_medico = DefaultRouter()
router_medico.register(r'', basename='medico', viewset=MedicoApiViewSet)