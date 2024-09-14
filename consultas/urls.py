from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='prueba'),
    path('resultados/<str:consulta>',views.evaluar_consultas,name='resultados'),
    path('buscar_tabla',views.buscar_tabla,name='buscar_tabla'),
    path('pagina_form',views.pagina_form,name='pagina_form'),
]
