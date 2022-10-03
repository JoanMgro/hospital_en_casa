from rest_framework.viewsets import ModelViewSet
from hec_backend.models.medico import Medico
from ..serializers.medicoSerializer import MedicoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class MedicoApiViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()