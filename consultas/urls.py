from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='evaluar_consultas'),
    path('evaluar_consultas/',views.evaluar_consultas,name='evaluar_consultas')
    
]
