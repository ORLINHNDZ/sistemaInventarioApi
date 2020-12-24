from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from sistemaInventarioApi.serializers import TipoProductoSerializer
from sistemaInventarioApi.models import TipoProducto


#Create Api TipoProducto
class tipoProductoCreate(generics.CreateAPIView):
    serializer_class = TipoProductoSerializer

#List Api TipoProducto
class tipoProductoList(generics.ListAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

#Update Api TipoProducto
class tipoProductoUpdate(generics.RetrieveUpdateAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

#Delete Api TipoProducto
class tipoProductoDelete(generics.DestroyAPIView):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer


