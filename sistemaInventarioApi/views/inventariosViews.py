from rest_framework import generics
from sistemaInventarioApi.serializers import InventarioSerializer
from sistemaInventarioApi.models import Inventario

#Create Api Inventario
class InventarioCreate(generics.CreateAPIView):
    serializer_class = InventarioSerializer

#List Api Inventario
class InventarioList(generics.ListAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

#Update Api Inventario
class InventarioUpdate(generics.RetrieveUpdateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

#Delete Api Inventario
class InventarioDelete(generics.DestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
