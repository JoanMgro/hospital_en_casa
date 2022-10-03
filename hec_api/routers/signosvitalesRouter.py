from ..views.signosvitalesCreateView import SignosVitalesViewSet
from rest_framework.routers import DefaultRouter


router_signos = DefaultRouter()
router_signos.register(r'',SignosVitalesViewSet, basename='signos_vitales')