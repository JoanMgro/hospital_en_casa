
from hec_backend.models.sugerencias_cuidado import SugerenciasCuidado
from ..serializers.sugerenciascuidadoSerializer import SugerenciasCuidadoSerializer

#librerias para viewSets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class SugerenciasViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = SugerenciasCuidadoSerializer
    queryset = SugerenciasCuidado.objects.all()