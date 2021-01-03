import django_filters.rest_framework
from rest_framework import generics
from sistemaInventarioApi.serializers import InventarioSerializer
from sistemaInventarioApi.models import Inventario
from rest_framework.permissions import IsAuthenticated

#Create Api Inventario
class InventarioCreate(generics.CreateAPIView):
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]
#List Api Inventario
class InventarioList(generics.ListAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['producto']
    permission_classes = [IsAuthenticated]

#Update Api Inventario
class InventarioUpdate(generics.RetrieveUpdateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]

#Delete Api Inventario
class InventarioDelete(generics.DestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [IsAuthenticated]
