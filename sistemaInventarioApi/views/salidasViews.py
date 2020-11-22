from rest_framework import generics
from sistemaInventarioApi.serializers import SalidasSerializer
from sistemaInventarioApi.models import Salida

#Create Api Pedidos
class SalidaCreate(generics.CreateAPIView):
    serializer_class = SalidasSerializer

#List Api Pedidos
class SalidaList(generics.ListAPIView):
    queryset = Salida.objects.all()
    serializer_class = SalidasSerializer

#Update Api Pedido
class SalidaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Salida.objects.all()
    serializer_class = SalidasSerializer

#Delete Api Pedido
class SalidaDelete(generics.DestroyAPIView):
    queryset = Salida.objects.all()
    serializer_class = SalidasSerializer