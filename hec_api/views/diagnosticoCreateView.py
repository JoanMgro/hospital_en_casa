
from hec_backend.models.diagnostico import Diagnostico
from ..serializers.diagnosticoSerializer import DiagnosticoSerializer

#librerias para viewSets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class DiagnosticoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = DiagnosticoSerializer
    queryset = Diagnostico.objects.all()
