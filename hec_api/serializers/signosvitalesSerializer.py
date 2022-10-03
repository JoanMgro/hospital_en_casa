from hec_backend.models.signos_vitales import SignosVitales
from rest_framework import serializers
from .userSerializer import UserSerializer

class SignosVitalesSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = SignosVitales
        fields = '__all__'
        