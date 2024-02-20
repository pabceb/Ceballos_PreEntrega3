from django.contrib import admin

# Register your models here.
from inicio.models import Producto, Cliente

admin.site.register([Producto, Cliente])
