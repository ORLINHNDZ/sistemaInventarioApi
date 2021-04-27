from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario, Roles, Producto, TipoProducto, Pedido, Inventario, Entrada, Salida, Descuento


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
        fields = ['id', 'genero', 'password', 'nombreUsuario', 'isActive', 'isAdmin', 'identidad',
                  'primerNombre', 'apellido', 'fechaNacimiento', 'genero',
                  'roles', 'correo', 'telefono', 'rtn', 'creacion', 'direccion',
                  'ultimaModificacion']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario (
            correo=validated_data['correo'],
            identidad=validated_data['identidad'],
            primerNombre=validated_data['primerNombre'],
            apellido=validated_data['apellido']
        )
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario

#Serializador TipoProducto
class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ['id', 'tipoProducto']

#Serializador Descuento
class DescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = ['id', 'descripcion', 'porcentaje']

#Serializador Producto
class ProductoSerializer(serializers.ModelSerializer):
    tipoPro = TipoProductoSerializer
    dec = DescuentoSerializer
    class Meta:
        model = Producto
        fields = ['id', 'tipoProducto', 'nombreProducto', 'imagen', 'marca', 'isv', 'nombrePopular',
                  'descripcionProducto', 'descuento', 'precio', 'cantidad']

#Serializador Pedido
class PedidoSeializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['producto', 'proveedor', 'cantidad', 'peso', 'estadoPedido']

#Serializador Inventario
class InventarioSerializer(serializers.ModelSerializer):
    tipoUsuarios: UsuarioSerializer
    tipoProductos: ProductoSerializer
    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'proveedor', 'precioCosto', 'precioVenta', 'existencia']

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





