from rest_framework.response import Response
from hec_backend.models.enfermero import Enfermero
from ..serializers.enfermeroSerializer import EnfermeroSerializer

#librerias para viewSets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class EnfermeroViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    serializer_class = EnfermeroSerializer
    queryset = Enfermero.objects.all()

