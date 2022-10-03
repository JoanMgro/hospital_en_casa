from ..views.userCreateView import UserViewSet
from rest_framework.routers import DefaultRouter


router_user = DefaultRouter()
router_user.register(r'',UserViewSet, basename='user')