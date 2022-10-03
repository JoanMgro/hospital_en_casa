from rest_framework.response import Response
from hec_backend.models.paciente import Paciente
from ..serializers.pacienteSerializer import PacienteSerializer

#librerias para viewSets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class PacienteViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

