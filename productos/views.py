from django.shortcuts import render
from .models import (
    Sabor, Mascopaleta, GalletaMascota,
    Picadita, Sanduche, Barbacoa,
    Licor
)

def inicio(request):
    return render(request, 'productos/inicio.html')


def lista_sabores(request):
    sabores = Sabor.objects.filter(disponible=True).order_by('categoria', 'nombre')
    
    # Agrupar sabores por categoría
    sabores_por_categoria = {}
    for sabor in sabores:
        categoria = sabor.categoria
        if categoria not in sabores_por_categoria:
            sabores_por_categoria[categoria] = []
        sabores_por_categoria[categoria].append(sabor)
    
    return render(request, 'productos/lista_sabores.html', {
        'sabores_por_categoria': sabores_por_categoria
    })

def lista_mascopaletas(request):
    mascopaletas = Mascopaleta.objects.filter(disponible=True)
    return render(request, 'productos/lista_mascopaletas.html', {
        'mascopaletas': mascopaletas
    })

def lista_galletas_mascota(request):
    galletas = GalletaMascota.objects.all()
    return render(request, 'productos/lista_galletas_mascota.html', {
        'galletas': galletas
    })

def lista_picaditas(request):
    picaditas = Picadita.objects.filter(disponible=True)
    return render(request, 'productos/lista_picaditas.html', {
        'picaditas': picaditas
    })

def lista_sanduches(request):
    sanduches = Sanduche.objects.filter(disponible=True)
    return render(request, 'productos/lista_sanduches.html', {
        'sanduches': sanduches
    })

def lista_barbacoa(request):
    platos_bbq = Barbacoa.objects.filter(disponible=True)
    return render(request, 'productos/lista_barbacoa.html', {
        'platos_bbq': platos_bbq
    })

def lista_licores(request):
    licores = Licor.objects.filter(disponible=True)
    return render(request, 'productos/lista_licores.html', {
        'licores': licores
    })

