from rest_framework.serializers import ModelSerializer
from .userSerializer import UserSerializer
from hec_backend.models.medico import Medico

class MedicoSerializer(ModelSerializer):
    user = UserSerializer() #Paso el serializador para guardar el user en el metodo custom create
    class Meta:
        model = Medico
        #fields = ('cedula', 'nombres')
        fields = '__all__'

    
        #Aca crear el custom create..
        # Primero se crea el user y luego el medico.
        #quien llama la funcion create? -> me parece que la llama el view.
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        validated_data['user'] = user_serializer.save()
        instance = super().create(validated_data)
        return instance