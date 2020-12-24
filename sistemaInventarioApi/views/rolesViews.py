from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from sistemaInventarioApi.serializers import RolesSerializer
from sistemaInventarioApi.models import Roles


#Create Api Roles
class RolesCreate(generics.CreateAPIView):
    serializer_class = RolesSerializer

#List Api Roles
class RolesList(generics.ListAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

#Update Api Roles
class RolesUpdate(generics.RetrieveUpdateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

#Delete Api Roles
class RolesDelete(generics.DestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer

