from django.urls import path, include
from . import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('inicio/', views.inicio, name='inicio'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('inscribir_carrera/', views.inscribir_carrera, name='inscribir_carrera'),

]