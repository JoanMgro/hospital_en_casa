from hec_backend.models.sugerencias_cuidado import SugerenciasCuidado
from rest_framework import serializers
from .userSerializer import UserSerializer

class SugerenciasCuidadoSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = SugerenciasCuidado
        fields = '__all__'
        