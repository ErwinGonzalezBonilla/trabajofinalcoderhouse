from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    return HttpResponse('<h1>Bienvenidos a tu Tienda de Trompetas ()>-iii-*</h1>') 

def about(request):
    return render(request, 'about.html') 
    
def mostrar_horario(request):
    fecha= datetime.now()
    return HttpResponse(f'Esta es la Fecha y Hora actual: {fecha}')

def saludo(request, nombre, apellido):
    nombre_formateado= nombre.title()
    apellido_formateado= apellido.title()
    return HttpResponse(f'Bienvenido/a  {nombre} {apellido}')


#


#from .models import Trompeta  # Asumiendo que tienes un modelo Trompeta definido en models.py


    #return render(request, 'inicio.html')

#def trompetas(request):
   # trompetas = Trompeta.objects.all()
  #  return render(request, 'trompetas.html', {'trompetas': trompetas})




#from django.http import HttpResponse
#from django.template import Template, Context, get_Template 
#from django.shortcuts import render

#def inicio(request):
    #def inicio(request):
       #return render(request, 'inicio.html')
#def trompetas(request):
   # def trompetas(request):
        #Trompetas = Trompetas.objects.all()
       # return render(request, 'trompetas.html')  
   
#    dicc =  {
#        'nombre' : 'Carlos',
#        'apellido' : 'Perez'
#    }  




#def saludo(request, nombre, apellido):
#    nombre_formateado = nombre.tittle()
 #   apellido_formateado = apellido.title()
    
#(f'Bienvenido/a {nombre_formateado}')




