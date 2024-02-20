from django.urls import path
from inicio.views import inicio, productos, clientes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('clientes/', clientes, name='clientes'),
]
