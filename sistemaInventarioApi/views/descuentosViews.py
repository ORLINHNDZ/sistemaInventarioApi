from rest_framework import generics
from sistemaInventarioApi.serializers import DescuentoSerializer
from sistemaInventarioApi.models import Descuento
from rest_framework.permissions import IsAuthenticated

#Create Api Pedidos
class DescuentoCreate(generics.CreateAPIView):
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticated]

#List Api Pedidos
class DescuentoList(generics.ListAPIView):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticated]

#Update Api Pedido
class DescuentoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticated]

#Delete Api Pedido
class DescuentoDelete(generics.DestroyAPIView):
    queryset = Descuento.objects.all()
    serializer_class = DescuentoSerializer
    permission_classes = [IsAuthenticated]