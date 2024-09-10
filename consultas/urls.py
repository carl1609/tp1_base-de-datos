from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.evaluar_consultas,name='evaluar_consultas'),
    
]
