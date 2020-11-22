from rest_framework import generics
from sistemaInventarioApi.serializers import EntradasSerializer
from sistemaInventarioApi.models import Entrada

#Create Api Pedidos
class EntradaCreate(generics.CreateAPIView):
    serializer_class = EntradasSerializer

#List Api Pedidos
class EntradaList(generics.ListAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradasSerializer

#Update Api Pedido
class EntradaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradasSerializer

#Delete Api Pedido
class EntradaDelete(generics.DestroyAPIView):
    queryset = Entrada.objects.all()
    serializer_class = EntradasSerializer