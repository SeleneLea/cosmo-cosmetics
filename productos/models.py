from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='Productos')
    stock = models.PositiveIntegerField(default=0)

    def __srt__(self):
        return self.nombre