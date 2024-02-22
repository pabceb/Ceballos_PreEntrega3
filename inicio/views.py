from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.template import Template, Context, loader

from inicio.models import Cliente, Producto
from inicio.forms import FormularioCrearProducto, FormularioCrearCliente

def inicio(request):
    # return HttpResponse('Ceballos - PreEntrega3')
    return render(request, 'inicio.html', {})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def crear_producto(request):
    formulario = FormularioCrearProducto()
    if request.method == 'POST':
        formulario = FormularioCrearProducto(request.POST)
        if formulario.is_valid():
            prod_id = formulario.cleaned_data.get('prod_id')
            nombre = formulario.cleaned_data.get('nombre')
            marca = formulario.cleaned_data.get('marca')
            precio = formulario.cleaned_data.get('precio')
            producto = Producto(prod_id = prod_id, nombre = nombre, marca = marca, precio = precio)
            producto.save()
            return redirect('productos')
    return render(request, 'crear_producto.html', {'formulario': formulario})

def crear_cliente(request):
    formulario = FormularioCrearCliente()
    if request.method == 'POST':
        formulario = FormularioCrearCliente(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            telefono = formulario.cleaned_data.get('telefono')
            cliente = Cliente(nombre = nombre, apellido = apellido, telefono = telefono)
            cliente.save()
            return redirect('clientes')
    return render(request, 'crear_cliente.html', {'formulario': formulario})

def mostrar_productos(request):
    return HttpResponse('Ceballos - PreEntrega3 - Productos')
#     productos = Producto.objects.all()
#     return render(request, 'productos.html', {'productos': productos})

def mostrar_clientes(request):
    return HttpResponse('Ceballos - PreEntrega3 - Clientes')
#     clientes = Cliente.objects.all()
#     return render(request, 'clientes.html', {'clientes': clientes})