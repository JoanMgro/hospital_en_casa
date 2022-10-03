from rest_framework.response import Response
from hec_backend.models.user import User
from ..serializers.userSerializer import UserSerializer

#librerias para permisos...
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny



#librerias para viewSets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

