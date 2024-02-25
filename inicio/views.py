from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.template import Template, Context, loader

from inicio.models import Cliente, Producto
from inicio.forms import FormularioCrearProducto, FormularioCrearCliente, BusquedaCliente, BusquedaProducto

def inicio(request):
    # return HttpResponse('Ceballos - PreEntrega3')
    return render(request, 'inicio.html', {})

def productos(request):
    # productos = Producto.objects.all()
    # se agrega formulario de busqueda (consultas --> GET)
    formulario = BusquedaProducto(request.GET)
    if formulario.is_valid():
        prod_a_buscar = formulario.cleaned_data.get('nombre')
        # productos = Producto.objects.filter(nombre = prod_a_buscar) 
        # se modifica para que sea por búsqueda parcial
        productos = Producto.objects.filter(nombre__icontains = prod_a_buscar)
    
    return render(request, 'productos.html', {'productos': productos, 'formulario': formulario})


def clientes(request):
    # Version 1 - sin busqueda
    # clientes = Cliente.objects.all()
    # return render(request, 'clientes.html', {'clientes': clientes})
    # Version 2 - CON busqueda
    formulario_cliente = BusquedaCliente(request.GET)
    if formulario_cliente.is_valid():
        cliente_buscado = formulario_cliente.cleaned_data.get('nombre')
        clientes = Cliente.objects.filter(nombre__icontains = cliente_buscado)
        
    return render(request, 'clientes.html', {'clientes': clientes, 'formulario_cliente': formulario_cliente})

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

def mostrar_clientes(request):
    return HttpResponse('Ceballos - PreEntrega3 - Clientes')