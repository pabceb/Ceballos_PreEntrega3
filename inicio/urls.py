from django.urls import path
from inicio.views import inicio, productos, clientes, crear_cliente, crear_producto, mostrar_clientes, mostrar_productos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('clientes/', clientes, name='clientes'),
    path('productos/crear-producto', crear_producto, name='crear_producto'),
    path('clientes/crear-cliente', crear_cliente, name='crear_cliente'),
    path('clientes/mostrar-productos', mostrar_productos, name='mostrar_productos'),
    path('clientes/mostrar-clientes', mostrar_clientes, name='mostrar_clientes'),
    
]