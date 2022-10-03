
from hec_backend.models.familiar import Familiar
from hec_backend.models.user import User
from rest_framework import serializers
from .userSerializer import UserSerializer
from .pacienteSerializer import PacienteSerializer

class FamiliarSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    #paciente = PacienteSerializer()
    class Meta:
        model = Familiar
        fields = '__all__'
    
    #Aca crear el custom create..puufff me exploto la cabeza esot funciono y no se como..
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        validated_data['user'] = user_serializer.save()
        instance = super().create(validated_data)
        return instance

        


        