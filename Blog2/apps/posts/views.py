from django.shortcuts import render
from .models import Producto, Categoria, Cliente

def inicio_post(request):
    # Tu lógica para la vista
    return render(request, 'Home.html')

def categorias_post(request):
    # Lógica para la página de categorías
    return render(request, 'posts/categorias.html')

def hombres_view(request):
    # Obtener productos de la categoría 'Hombres'
    productos_hombres = Producto.objects.filter(categoria__tipo='H')
    return render(request, 'barra/hombres.html', {'productos': productos_hombres})

def mujeres_view(request):
    # Obtener productos de la categoría 'Mujeres'
    productos_mujeres = Producto.objects.filter(categoria__tipo='M')
    return render(request, 'barra/mujeres.html', {'productos': productos_mujeres})

def ninos_view(request):
    # Obtener productos de la categoría 'Niños'
    productos_ninos = Producto.objects.filter(categoria__tipo='N')
    return render(request, 'barra/ninos.html', {'productos': productos_ninos})

def ofertas_view(request):
    # Obtener productos en oferta (puedes tener un campo 'en_oferta' en tu modelo Producto)
    productos_oferta = Producto.objects.filter(en_oferta=True)
    return render(request, 'barra/ofertas.html', {'productos': productos_oferta})

def contacto_view(request):
    return render(request, 'barra/contacto.html')
