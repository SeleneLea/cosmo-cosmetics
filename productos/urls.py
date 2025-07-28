from django.urls import path
from .views import lista_productos, detalle_producto, vista_ofertas, vista_nosotros

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('ofertas/', vista_ofertas, name='ofertas'),
    path('<int:id>/', detalle_producto, name='detalle_producto'),
    path('nosotros/', vista_nosotros, name='nosotros'),
]



