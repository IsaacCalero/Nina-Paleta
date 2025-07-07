from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # ← esta es la raíz
    path('sabores/', views.lista_sabores, name='lista_sabores'),
    path('mascopaletas/', views.lista_mascopaletas, name='mascopaletas'),
    path('galletas-mascota/', views.lista_galletas_mascota, name='lista_galletas_mascota'),
    path('picaditas/', views.lista_picaditas, name='lista_picaditas'),
    path('sanduches/', views.lista_sanduches, name='lista_sanduches'),
    path('barbacoa/', views.lista_barbacoa, name='lista_barbacoa'),
    path('licores/', views.lista_licores, name='lista_licores'),
]

