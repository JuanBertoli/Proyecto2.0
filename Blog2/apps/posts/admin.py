# apps/posts/admin.py
from django.contrib import admin
from .models import Categoria, Producto  # Cambia 'Post' por 'Producto'

admin.site.register(Categoria)
admin.site.register(Producto)
# Agrega otras configuraciones de admin según sea necesario

