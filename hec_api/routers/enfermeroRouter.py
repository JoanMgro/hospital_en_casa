from ..views.enfermeroCreateView import EnfermeroViewSet
from rest_framework.routers import DefaultRouter


router_enfermero = DefaultRouter()
router_enfermero.register(r'',EnfermeroViewSet, basename='enfermero')