from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Categorías posibles para sabores
CATEGORIAS_SABOR = [
    ('Frutales', 'Frutales'),
    ('Miche Mix', 'Miche Mix'),
    ('Yogurt', 'Yogurt'),
    ('Con Licor', 'Con Licor'),
    ('Autóctonos', 'Autóctonos'),
    ('Temporada', 'Temporada'),
    ('Mascotas', 'Mascotas'),
    ('Sin Azúcar', 'Sin Azúcar'),
]

class Sabor(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=[
        ('miche_mix', 'Miche Mix'),
        ('yogurt', 'Paletas de Yogurt'),
        ('licor', 'Paletas con Licor'),
        ('frutales', 'Paletas Frutales')
    ])
    descripcion = models.TextField(blank=True, null=True)
    precio_pequeno = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    precio_grande = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    disponible = models.BooleanField(default=True)
    especial = models.BooleanField(default=False)
    temporada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre



class Topping(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nombre
    


class Paleta(models.Model):
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping, blank=True)
    chocolate_bañado = models.BooleanField(default=False)
    imagen_personalizada = models.ImageField(upload_to='paletas/', blank=True, null=True)

    

    def calcular_precio_total(self):
        total = self.sabor.precio_grande if self.chocolate_bañado else self.sabor.precio_pequeno
        total += sum(t.precio for t in self.toppings.all())
        return total

    def __str__(self):
        return f"Paleta de {self.sabor.nombre}"
    

class Mascopaleta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    tamano = models.CharField(max_length=50, choices=[
        ('Pequeña', 'Pequeña'),
        ('Mediana', 'Mediana'),
        ('Grande', 'Grande'),
    ])
    sin_lactosa = models.BooleanField(default=True)
    sin_azucar = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='mascopaletas/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.tamano})"


class GalletaMascota(models.Model):
    sabor = models.CharField(max_length=100)  # Ej. Carne, Pollo, Cerdo
    tamaño = models.CharField(max_length=50, default="Estándar")
    ingredientes = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    imagen = models.ImageField(upload_to='galletas_mascota/', blank=True, null=True)

    def __str__(self):
        return f"Galleta de {self.sabor}"


class Sanduche(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo_pan = models.CharField(max_length=50, blank=True)  # Ej. Baguette, Brioche
    incluye_papas = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='sanduches/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Barbacoa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    peso_carne = models.IntegerField(help_text="Cantidad en gramos")
    incluye_papas = models.BooleanField(default=True)
    incluye_ensalada = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='barbacoa/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Picadita(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    porciones = models.CharField(max_length=50, blank=True)  # Ej. "Ideal para 3 personas"
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='picaditas/', blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    
class Licor(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('Vino', 'Vino'),
        ('Whisky', 'Whisky'),
        ('Tequila', 'Tequila'),
        ('Ron', 'Ron'),
        ('Aguardiente', 'Aguardiente'),
        ('Fernet', 'Fernet'),
        ('Otro', 'Otro')
    ])
    descripcion = models.TextField(blank=True)
    incluye = models.TextField(blank=True)  # Ej. "2L de gaseosa negra y hielos"
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='licores/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)




class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField()
    producto = GenericForeignKey('content_type', 'object_id')
    cantidad = models.PositiveIntegerField(default=1)


class Adicional(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre







