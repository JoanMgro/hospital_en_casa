from hec_backend.models.diagnostico import Diagnostico
from rest_framework import serializers


class DiagnosticoSerializer(serializers.ModelSerializer):

      
    class Meta:
        model = Diagnostico
        fields = '__all__'
        