from rest_framework import generics
from sistemaInventarioApi.serializers import InventarioSerializer
from sistemaInventarioApi.models import Inventario

#Create Api Pedidos
class InventarioCreate(generics.CreateAPIView):
    serializer_class = InventarioSerializer

#List Api Pedidos
class InventarioList(generics.ListAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

#Update Api Pedido
class InventarioUpdate(generics.RetrieveUpdateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

#Delete Api Pedido
class InventarioDelete(generics.DestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
