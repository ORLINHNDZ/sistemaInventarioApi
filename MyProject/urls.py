from django.urls import include, path
from sistemaInventarioApi.views.usuariosViews import UsuarioCreate, UsuarioList, UsuarioUpdate, UsuarioDelete
from sistemaInventarioApi.views.productosViews import ProductoCreate, ProductoList, ProductoUpdate, ProductoDelete
from sistemaInventarioApi.views.pedidosViews import PedidosCreate, PedidosList, PedidosUpdate, PedidosDelete
from sistemaInventarioApi.views.inventariosViews import InventarioCreate, InventarioList, InventarioUpdate, InventarioDelete
from sistemaInventarioApi.views.entradasViews import EntradaCreate, EntradaList, EntradaUpdate, EntradaDelete
from sistemaInventarioApi.views.salidasViews import SalidaCreate, SalidaList, SalidaUpdate, SalidaDelete
from sistemaInventarioApi.views.tipoProductosViews import tipoProductoCreate, tipoProductoList, tipoProductoUpdate, tipoProductoDelete
from sistemaInventarioApi.views.rolesViews import RolesCreate, RolesList, RolesUpdate, RolesDelete

from rest_framework import routers

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Usuarios Paths
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/usuarios', UsuarioList.as_view(), name='usuarios_list'),
    path('api/usuarios/create', UsuarioCreate.as_view(), name='usuarios_create'),
    path('api/usuarios/<int:pk>/edit', UsuarioUpdate.as_view(), name='usuarios_update'),
    path('api/usuarios/<int:pk>/delete', UsuarioDelete.as_view(), name='usuarios_delete'),
    # Productos Paths
    path('api/roles', RolesList.as_view(), name='roles_list'),
    path('api/roles/create', RolesCreate.as_view(), name='roles_create'),
    path('api/roles/<int:pk>/edit', RolesUpdate.as_view(), name='roles_update'),
    path('api/roles/<int:pk>/delete', RolesDelete.as_view(), name='roles_delete'),
    # Productos Paths
    path('api/productos', ProductoList.as_view(), name='productos_list'),
    path('api/productos/create', ProductoCreate.as_view(), name='productos_create'),
    path('api/productos/<int:pk>/edit', ProductoUpdate.as_view(), name='productos_update'),
    path('api/productos/<int:pk>/delete', ProductoDelete.as_view(), name='productos_delete'),
    # Productos Paths
    path('api/tipoProductos', tipoProductoList.as_view(), name='tipoProductos_list'),
    path('api/tipoProductos/create', tipoProductoCreate.as_view(), name='tipoProductos_create'),
    path('api/tipoProductos/<int:pk>/edit', tipoProductoUpdate.as_view(), name='tipoProductos_update'),
    path('api/tipoProductos/<int:pk>/delete', tipoProductoDelete.as_view(), name='tipoProductos_delete'),
    # Pedidos Paths
    path('api/pedidos', PedidosList.as_view(), name='pedidos_list'),
    path('api/pedidos/create', PedidosCreate.as_view(), name='pedidos_create'),
    path('api/pedidos/<int:pk>', PedidosUpdate.as_view(), name='pedidos_update'),
    path('api/pedidos/<int:pk>/delete', PedidosDelete.as_view(), name='pedidos_delete'),
    # Inventarios Paths
    path('api/inventario', InventarioList.as_view(), name='inventario_list'),
    path('api/inventario/create', InventarioCreate.as_view(), name='inventario_create'),
    path('api/inventario/<int:pk>/edit', InventarioUpdate.as_view(), name='inventario_update'),
    path('api/inventario/<int:pk>/delete', InventarioDelete.as_view(), name='inventario_delete'),
    # Entradas Paths
    path('api/entradas', EntradaList.as_view(), name='entrada_list'),
    path('api/entradas/create', EntradaCreate.as_view(), name='entrada_create'),
    path('api/entradas/<int:pk>/edit', EntradaUpdate.as_view(), name='entrada_update'),
    path('api/entradas/<int:pk>/delete', EntradaDelete.as_view(), name='entrada_delete'),
    # Salida Paths
    path('api/salidas', SalidaList.as_view(), name='salida_list'),
    path('api/salidas/create', SalidaCreate.as_view(), name='salida_create'),
    path('api/salidas/<int:pk>/edit', SalidaUpdate.as_view(), name='salida_update'),
    path('api/salidas/<int:pk>/delete', SalidaDelete.as_view(), name='salida_delete'),

]
