from django.contrib import admin

from django.contrib import admin
from .models import (
    Sabor, Topping, Paleta,
    Mascopaleta, GalletaMascota,
    Sanduche, Barbacoa, Picadita,
    Licor, Adicional
)

@admin.register(Sabor)
class SaborAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'especial', 'temporada', 'disponible')
    list_filter = ('categoria', 'especial', 'temporada', 'disponible')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)

@admin.register(Paleta)
class PaletaAdmin(admin.ModelAdmin):
    list_display = ('sabor', 'chocolate_bañado')
    filter_horizontal = ('toppings',)

@admin.register(Mascopaleta)
class MascopaletaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tamano', 'precio', 'sin_lactosa', 'sin_azucar')
    list_filter = ('tamano', 'sin_lactosa', 'sin_azucar')

@admin.register(GalletaMascota)
class GalletaMascotaAdmin(admin.ModelAdmin):
    list_display = ('sabor', 'tamaño', 'precio')
    search_fields = ('sabor',)

@admin.register(Sanduche)
class SanducheAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_pan', 'incluye_papas', 'precio', 'disponible')
    list_filter = ('tipo_pan', 'incluye_papas', 'disponible')

@admin.register(Barbacoa)
class BarbacoaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'peso_carne', 'incluye_papas', 'incluye_ensalada', 'precio')
    list_filter = ('incluye_papas', 'incluye_ensalada')

@admin.register(Picadita)
class PicaditaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'porciones', 'precio', 'disponible')
    list_filter = ('disponible',)

@admin.register(Licor)
class LicorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'disponible')
    list_filter = ('tipo', 'disponible')
    search_fields = ('nombre',)

admin.site.register(Adicional)
