from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def index(request):
    return render(request,'base.html')

def evaluar_consultas(request,consulta,grafico):
    consultas={
        #aqui van las consultas
        "consulta1":"select * from conejos",
    }
    

    #funcion para obtener la consulta me devuelve una lista de duplas con los resultados
    def obtener_consulta(consulta):
        with connection.cursor() as cursor:
            cursor.execute(consultas[consulta])
            resultado=cursor.fetchall()
            nombre_columnas=[desc[0] for desc in cursor.description]
        return resultado,nombre_columnas
    
    resultado,nombre_columnas=obtener_consulta(consulta) 
    lista_resultado=[list(tupla) for tupla in resultado]
    hay_grafico='no' if grafico==0 else 'si' 
    print(lista_resultado)
    return render(request,'resultado.html',{'resultados':lista_resultado,'columnas':nombre_columnas,'grafico':grafico})



 