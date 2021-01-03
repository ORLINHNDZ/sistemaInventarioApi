from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import django_filters.rest_framework
from rest_framework import generics
from sistemaInventarioApi.serializers import ProductoSerializer
from sistemaInventarioApi.models import Producto
from rest_framework.permissions import IsAuthenticated


#Create Api Producto
class ProductoCreate(generics.CreateAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

#List Api Producto
class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['nombreProducto']
    permission_classes = [IsAuthenticated]


#Update Api Producto
class ProductoUpdate(generics.RetrieveUpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

#Delete Api Producto
class ProductoDelete(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]


