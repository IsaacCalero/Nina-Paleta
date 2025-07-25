from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sabores/', views.lista_sabores, name='lista_sabores'),
    path('galletas-mascota/', views.lista_galletas_mascota, name='lista_galletas_mascota'),
    path('picaditas/', views.lista_picaditas, name='lista_picaditas'),
    path('sanduches/', views.lista_sanduches, name='lista_sanduches'),
    path('licores/', views.lista_licores, name='lista_licores'),

    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<str:app_label>/<str:model_name>/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<str:app_label>/<str:model_name>/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]


