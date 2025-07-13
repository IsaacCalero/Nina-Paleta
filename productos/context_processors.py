from .models import Pedido

def carrito_context(request):
    carrito = None
    if request.user.is_authenticated:
        carrito = Pedido.objects.filter(usuario=request.user).order_by('-creado_en').first()
    return {'carrito': carrito}

