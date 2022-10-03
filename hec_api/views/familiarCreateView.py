from rest_framework.response import Response
from hec_backend.models.familiar import Familiar
from ..serializers.familiarSerializer import FamiliarSerializer

#librerias para viewSets
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

class FamiliarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = FamiliarSerializer
    queryset = Familiar.objects.all()






# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from ..models.familiar import Familiar
# from ..serializers.familiarSerializer import FamiliarSerializer


# @api_view(['GET', 'POST'])
# def familiar_list(request):
#     if request.method == 'GET':
#         familiares = Familiar.objects.all()
#         serializer = FamiliarSerializer(familiares, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = FamiliarSerializer(data=request.data)
#         if serializer.is_valid():
            
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

