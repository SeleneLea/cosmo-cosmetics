from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib import messages
from .models import Producto, Categoria
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def lista_productos(request, categoria_id=None):
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id, stock__gt=0)
    else:
        # mostramos todos los productos
        productos = Producto.objects.filter(stock__gt=0)

    categorias = Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias': categorias,
        'categoria_seleccionada_id': categoria_id # Pasamos el ID para saber cuál está activa
    }
    return render(request, 'productos/lista_productos.html', context)

def vista_ofertas(request):
    return render(request, 'productos/ofertas.html')

def vista_nosotros(request):
    return render(request, 'productos/nosotros.html')

def detalle_producto(request,id):
    producto = get_object_or_404(Producto, pk=id)
    context = {
        'producto': producto
    }
    return render(request, 'productos/detalle_producto.html', context)

def vista_cuenta(request):
    return render(request, 'productos/en_construccion.html', {'pagina': 'Mi Cuenta'})

def agregar_al_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    cantidad = int(request.POST.get('cantidad', 1))
    
    carrito = request.session.get('carrito', {})
    
    # Si el producto ya está en el carrito, actualizamos la cantidad
    if str(id) in carrito:
        carrito[str(id)]['cantidad'] += cantidad
    else:
        carrito[str(id)] = {'cantidad': cantidad, 'precio': str(producto.precio)}
        
    request.session['carrito'] = carrito
    messages.success(request, f'¡Se agregó {producto.nombre} al carrito!')
    
    return redirect('lista_productos')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_en_carrito = []
    total = 0

    for id, item in carrito.items():
        producto = get_object_or_404(Producto, id=id)
        subtotal = producto.precio * item['cantidad']
        total += subtotal
        productos_en_carrito.append({
            'producto': producto,
            'cantidad': item['cantidad'],
            'precio_unitario': producto.precio,
            'subtotal': subtotal
        })

    context = {
        'productos_en_carrito': productos_en_carrito,
        'total': total
    }
    return render(request, 'productos/carrito.html', context)

#vista para la logica de compra
def comprar(request):
    carrito = request.session.get('carrito', {})
    for id, item in carrito.items():
        producto = get_object_or_404(Producto, id=id)
        if producto.stock >= item['cantidad']:
            producto.stock -= item['cantidad']
            producto.save()
        else:
            messages.error(request, f'No hay suficiente stock para {producto.nombre}')
            return redirect('ver_carrito')
    
    # limpiar el carrito después de la compra
    request.session['carrito'] = {}
    messages.success(request, '¡Compra realizada exitosamente!')
    return redirect('lista_productos')

def vista_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login') # Redirigimos al login
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required # este decorador protege la página
def vista_cuenta(request):
    return render(request, 'productos/cuenta.html')


