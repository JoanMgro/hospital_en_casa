from ..views.familiarCreateView import FamiliarViewSet
from rest_framework.routers import DefaultRouter


router_familiar = DefaultRouter()
router_familiar.register(r'',FamiliarViewSet, basename='familiar')