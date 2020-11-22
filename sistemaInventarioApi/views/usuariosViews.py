from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from sistemaInventarioApi.serializers import UsuarioSerializer
from sistemaInventarioApi.models import Usuario

#Create Api Usuario
class UsuarioCreate(generics.CreateAPIView):
    serializer_class = UsuarioSerializer

#List Api Usuario
class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#Update Api Usuario
class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#Delete Api View
class UsuarioDelete(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

