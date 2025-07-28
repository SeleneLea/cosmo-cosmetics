from django.shortcuts import render, get_list_or_404
from .models import Producto, Categoria
# Create your views here.

def lista_productos(request):
    productos = Producto.objects.all() #todos los obj productos de la bd

    categorias = Categoria.objects.all() #y las categorias para los filtros
    context = {
        'productos': productos,
        'categorias': categorias, # Las añadimos al contexto
    }
    return render(request, 'productos/lista_productos.html',context)

def vista_ofertas(request):
    return render(request, 'productos/en_construccion.html', {'pagina': 'Ofertas'})

def vista_nosotros(request):
    return render(request, 'productos/en_construccion.html', {'pagina': 'Acerca de Nosotros'})

def detalle_producto(request,id):
    producto = get_object_or_404(Producto, pk=id)
    context = {
        'producto': producto
    }
    return render(request, 'productos/detalle_producto.html', context)


