from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # opcional: inicia sesión automáticamente
            return redirect('lista_sabores')  # o a donde quieras
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})

from django.contrib.auth.decorators import login_required
from .models import (
    Sabor, GalletaMascota,
    Picadita, Sanduche, Barbacoa,
    Licor, Pedido, ItemPedido
)

def inicio(request):
    return render(request, 'productos/inicio.html')


from .models import Sabor, Mascopaleta

def lista_sabores(request):
    sabores = Sabor.objects.filter(disponible=True).order_by('categoria', 'nombre')
    mascopaletas = Mascopaleta.objects.filter(disponible=True).order_by('nombre')

    # Agrupar sabores por categoría
    sabores_por_categoria = {}
    for sabor in sabores:
        categoria = sabor.categoria
        if categoria not in sabores_por_categoria:
            sabores_por_categoria[categoria] = []
        sabores_por_categoria[categoria].append(sabor)

    return render(request, 'productos/lista_sabores.html', {
        'sabores_por_categoria': sabores_por_categoria,
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


def lista_licores(request):
    licores = Licor.objects.filter(disponible=True)
    return render(request, 'productos/lista_licores.html', {
        'licores': licores
    })

@login_required
def agregar_al_carrito(request):
    if request.method == 'POST':
        sabor_id = request.POST['sabor_id']
        tamano = request.POST['tamano']
        cantidad = int(request.POST['cantidad'])

        sabor = Sabor.objects.get(id=sabor_id)
        pedido, _ = Pedido.objects.get_or_create(usuario=request.user, activo=True)
        ItemPedido.objects.create(pedido=pedido, sabor=sabor, tamaño=tamano, cantidad=cantidad)

        return redirect('sabores')

@login_required
def ver_carrito(request):
    try:
        # Busca el pedido activo del usuario
        pedido = Pedido.objects.get(usuario=request.user, activo=True)
        items = pedido.items.select_related('sabor')  # optimiza la carga
    except Pedido.DoesNotExist:
        pedido = None
        items = []

    # Calcula el total
    total = sum(item.sabor.precio_pequeno if item.tamaño == 'pequeño' else item.sabor.precio_grande for item in items)

    context = {
        'pedido': pedido,
        'items': items,
        'total': total,
    }

    return render(request, 'carrito.html', context)


def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # opcional: inicia sesión automáticamente
            return redirect('lista_sabores')  # o a donde quieras
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')  # o la página que elijas después de cerrar sesión
