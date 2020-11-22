from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario, Roles, Producto, TipoProducto, Pedido, Inventario, Entrada, Salida


#Seralizador Roles
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


#Serializador Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolesSerializer
    class Meta:
        model = Usuario
        fields = ['genero', 'nombre_usuario', 'is_active', 'is_admin', 'identidad',
                  'primer_nombre', 'segundo_apellido', 'fecha_nacimiento', 'genero',
                  'roles', 'correo', 'telefono', 'cedula', 'rtn', 'creacion', 'direccion',
                  'ultima_modificacion']

#Serializador TipoProducto
class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ['Abarroteria', 'Repuestos', 'Comida']

#Serializador Producto
class ProductoSerializer(serializers.ModelSerializer):
    tipoPro = TipoProductoSerializer
    class Meta:
        model = Producto
        fields = ['tipoProducto', 'nombreProducto', 'imagen', 'marca', 'isv', 'nombrePopular',
                  'descripcionProducto']

#Serializador Pedido
class PedidoSeializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['producto', 'proveedor', 'cantidad', 'peso', 'estadoPedido']

#Serializador Inventario
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = ['producto', 'proveedor', 'precioCosto', 'precioVenta', 'existencia']

#Serializador Entradas
class EntradasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = ['producto', 'estadoPedido', 'fecha', 'precioCosto', 'cantidad',
                  'numeroFactura']

class SalidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salida
        fields = ['factura', 'tipoSalida', 'fecha', 'precio','cantidad']




