from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Picadita
from django.http import HttpResponseBadRequest
from django.contrib import messages
from .models import Sabor, Mascopaleta
from productos.models import Sabor

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





def lista_sabores(request):
    sabores = Sabor.objects.filter(disponible=True).order_by('categoria', 'nombre')
    categorias = [
        ('miche_mix', '🥭 Miche Mix'),
        ('yogurt', '🍓 Paletas de Yogurt'),
        ('licor', '🍹 Paletas con Licor')
    ]
    return render(request, 'productos/lista_sabores.html', {
        'sabores': sabores,
        'categorias': categorias
    })




def lista_galletas_mascota(request):
    galletas = GalletaMascota.objects.all()
    return render(request, 'productos/lista_galletas_mascota.html', {
        'galletas': galletas
    })


def lista_picaditas(request):
    productos = Picadita.objects.filter(disponible=True)
    return render(request, 'productos/lista_picaditas.html', {'productos': productos})



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
def agregar_al_carrito(request, app_label, model_name, producto_id):
    producto_type = ContentType.objects.get(app_label=app_label, model=model_name)
    
    carrito = request.session.get('carrito', {})

    # 👇 Captura el tamaño desde el formulario (por defecto: 'pequeno')
    tamano = request.POST.get('tamano', 'pequeno')

    # 👇 Crea una clave única incluyendo el tamaño
    key = f"{producto_type.id}:{producto_id}:{tamano}"
    carrito[key] = carrito.get(key, 0) + 1

    request.session['carrito'] = carrito

    print("Contenido del carrito:", carrito)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    items = []
    total = 0

    for key, cantidad in carrito.items():
        try:
            # 👇 Captura content_type_id, producto_id y tamaño desde la clave
            content_type_id, object_id, tamano = key.split(':')

            content_type = ContentType.objects.get_for_id(int(content_type_id))
            modelo = content_type.model_class()
            producto = modelo.objects.get(id=int(object_id))

            # 👇 Cálculo de precio según tamaño
            if tamano == 'grande':
                precio_unitario = producto.precio_grande
            else:
                precio_unitario = producto.precio_pequeno

            subtotal = precio_unitario * cantidad

            items.append({
                'producto': producto,
                'cantidad': cantidad,
                'tamano': tamano.capitalize(),
                'precio_unitario': precio_unitario,
                'subtotal': subtotal,
                'model_name': producto.__class__.__name__.lower(),
            })

            total += subtotal
        except Exception as e:
            print(f"Error al reconstruir item del carrito: {e}")
            continue

    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'carrito.html', context)



@login_required
def agregar_al_carrito(request, app_label, model_name, producto_id):
    try:
        producto_type = ContentType.objects.get(app_label=app_label, model=model_name)
        modelo = producto_type.model_class()

        producto = modelo.objects.filter(id=producto_id, disponible=True).first()
        if not producto:
            return HttpResponseBadRequest("El producto solicitado no existe o no está disponible.")

        carrito = request.session.get('carrito', {})
        key = f"{producto_type.id}:{producto_id}"
        carrito[key] = carrito.get(key, 0) + 1
        request.session['carrito'] = carrito

        messages.success(request, f"¡{producto.nombre} agregado al carrito!")

        print("Producto válido. Carrito actualizado:", carrito)
        return redirect(request.META.get('HTTP_REFERER', '/'))

    except ContentType.DoesNotExist:
        return HttpResponseBadRequest("Tipo de producto no válido.")
    
@login_required
def eliminar_del_carrito(request, app_label, model_name, producto_id):
    producto_type = ContentType.objects.get(app_label=app_label, model=model_name)
    key = f"{producto_type.id}:{producto_id}"
    carrito = request.session.get('carrito', {})

    if key in carrito:
        carrito.pop(key)
        request.session['carrito'] = carrito
        from django.contrib import messages
        messages.success(request, "Producto eliminado del carrito.")

    return redirect('ver_carrito')



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
