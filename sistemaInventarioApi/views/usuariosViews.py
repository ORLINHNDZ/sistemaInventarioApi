from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
import django_filters.rest_framework
from rest_framework import generics
from sistemaInventarioApi.serializers import UsuarioSerializer
from sistemaInventarioApi.models import Usuario
from rest_framework.permissions import IsAuthenticated

#Create Api Usuario
class UsuarioCreate(generics.CreateAPIView):
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

#List Api Usuario
class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['nombreUsuario']
    permission_classes = [IsAuthenticated]

#Update Api Usuario
class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

#Delete Api View
class UsuarioDelete(generics.DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

