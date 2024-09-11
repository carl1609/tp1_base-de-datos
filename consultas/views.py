from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
# Create your views here.

def index(request):
    return render(request,'index.html')

def evaluar_consultas(request):
    consultas={
        #aqui van las consultas
        "consulta1":"select * from conejos",
    }
    consulta=request.POST.get('consulta')
    #funcion para obtener la consulta me devuelve una lista de duplas con los resultados
    def obtener_consulta(consulta):
        with connection.cursor() as cursor:
            cursor.execute(consultas[consulta])
            resultado=cursor.fetchall()
        return resultado
    
    resultado=obtener_consulta(consulta)

    return render(request,'resultado.html',{'resultados':resultado})



