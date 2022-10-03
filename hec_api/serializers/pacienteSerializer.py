
from hec_backend.models.paciente import Paciente
from rest_framework import serializers
from .userSerializer import UserSerializer
from .medicoSerializer import MedicoSerializer
from .enfermeroSerializer import EnfermeroSerializer

class PacienteSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    #medico = MedicoSerializer()
    #enfermero = EnfermeroSerializer()

    class Meta:
        model = Paciente
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        validated_data['user'] = user_serializer.save()
        instance = super().create(validated_data)
        return instance

