from django.urls import path
from .views import (
    lista_productos, detalle_producto, vista_ofertas, 
    vista_nosotros, vista_cuenta, agregar_al_carrito, ver_carrito, comprar
)

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('categoria/<int:categoria_id>/', lista_productos, name='filtrar_por_categoria'),
    path('<int:id>/', detalle_producto, name='detalle_producto'),
    path('ofertas/', vista_ofertas, name='ofertas'),
    path('nosotros/', vista_nosotros, name='nosotros'),
    path('cuenta/', vista_cuenta, name='cuenta'),
    # Nuevas rutas para el carrito
    path('agregar/<int:id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('comprar/', comprar, name='comprar'),
]



