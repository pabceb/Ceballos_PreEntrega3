from django import forms

class FormularioCrearProducto(forms.Form):
    prod_id = forms.IntegerField()
    nombre = forms.CharField(max_length = 20)
    marca = forms.CharField(max_length = 20)
    precio = forms.FloatField()   
    
class FormularioCrearCliente(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 20)
    telefono = forms.IntegerField()

class BusquedaCliente(forms.Form):
    nombre = forms.CharField(max_length = 20, required=False)

class BusquedaProducto(forms.Form):
    nombre = forms.CharField(max_length = 20, required=False)