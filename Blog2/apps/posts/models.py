# En tu archivo models.py en la aplicación posts
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    TIPO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('N', 'Niño'),
        ('O', 'Oferta'),
    ]
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    en_oferta = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='DetallePedido')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    completado = models.BooleanField(default=False)

class DetallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class Resena(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
