from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template import Template, Context, loader

from inicio.models import Cliente, Producto
from inicio.forms import FormularioCrearProducto, FormularioCrearCliente

def inicio(request):
    # return HttpResponse('Ceballos - PreEntrega3')
    return render(request, 'inicio.html', {})

def productos(request):
    return render(request, 'productos.html', {})

def clientes(request):
    return render(request, 'clientes.html', {})

def crear_producto(request):
    formulario = FormularioCrearProducto()
    if request.method == 'POST':
        formulario = FormularioCrearProducto(request.POST)
        prod_id = formulario.cleaned_data.get('prod_id')
        nombre = formulario.cleaned_data.get('nombre')
        marca = formulario.cleaned_data.get('marca')
        precio = formulario.cleaned_data.get('precio')
        producto = Producto(prod_id = prod_id, nombre = nombre, marca = marca, precio = precio)
        producto.save()
        return redirect('productos.html')
    return render(request, 'productos.html', {'formulario': formulario})
    # return render(request, 'crear_producto. html', {'formulario': formulario})

def crear_cliente(request):
    formulario = FormularioCrearCliente()
    if request.method == 'POST':
        formulario = FormularioCrearCliente(request.POST)
        nombre = formulario.cleaned_data.get('nombre')
        apellido = formulario.cleaned_data.get('apellido')
        telefono = formulario.cleaned_data.get('telefono')
        cliente = Cliente(nombre = nombre, apellido = apellido, telefono = telefono)
        cliente.save()
        return redirect('clientes.html')
    return render(request, 'clientes.html', {'formulario': formulario})
    # return render(request, 'crear_clientes. html', {'formulario': formulario})

def mostrar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'mostrar_producto.html', {'productos': productos})

def mostrar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'mostrar_clientes.html', {'clientes': clientes})