
from hec_backend.models.signos_vitales import SignosVitales
from ..serializers.signosvitalesSerializer import SignosVitalesSerializer

#librerias para viewSets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class SignosVitalesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = SignosVitalesSerializer
    queryset = SignosVitales.objects.all()

