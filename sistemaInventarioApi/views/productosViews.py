from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from sistemaInventarioApi.serializers import ProductoSerializer
from sistemaInventarioApi.models import Producto


#Create Api Producto
class ProductoCreate(generics.CreateAPIView):
    serializer_class = ProductoSerializer

#List Api Producto
class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#Update Api Producto
class ProductoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#Delete Api Producto
class ProductoDelete(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
