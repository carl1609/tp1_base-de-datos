from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='prueba'),
    path('resultados/<str:consulta>/',views.evaluar_consultas,name='resultados')
    
]
