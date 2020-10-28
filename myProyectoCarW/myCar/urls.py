from django.contrib import admin
from django.urls import path, include
from .views import inicio,galeria,formulario,formulario2,quienes_somos,login,cerrar_sesion,lista_insumos,eliminar,busqueda_mod,modificar

urlpatterns = [
    path('',inicio,name='INICIO'),
    path('galeria/',galeria,name='GALERIA'),
    path('formulario/',formulario,name='FORMULARIO'),
    path('formulario2/',formulario2,name='FORMULARIO2'),
    path('quienes_somos/',quienes_somos,name='QUIENES_SOMOS'),
    path('login/',login,name='LOGIN'),
    path('cerrar_sesion/',cerrar_sesion,name='LOGOUT'),
    path('lista_insumos/',lista_insumos,name='LISTAINSUMO'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('buscar/<id>/',busqueda_mod,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR'),
]