
from rest_framework import serializers
from hec_backend.models.user import User


class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        exclude = [
            'is_superuser',
            'last_login',
            'groups',
            'user_permissions',
            'is_active',
            'is_staff'
        
        
        ]
        extra_kwargs = {'password': {'write_only': True}} #esto es para que salga en el listado del view.
        

