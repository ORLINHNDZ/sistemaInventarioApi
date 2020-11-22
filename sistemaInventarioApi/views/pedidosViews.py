from rest_framework import generics
from sistemaInventarioApi.serializers import PedidoSeializer
from sistemaInventarioApi.models import Pedido

#Create Api Pedidos
class PedidosCreate(generics.CreateAPIView):
    serializer_class = PedidoSeializer

#List Api Pedidos
class PedidosList(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSeializer

#Update Api Pedido
class PedidosUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSeializer

#Delete Api Pedido
class PedidosDelete(generics.DestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSeializer
