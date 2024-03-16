from django.urls import path
from inicio.views import inicio, mostrar_horario, saludo


#from . import views

urlpatterns = [
   path('', inicio, name='inicio'),
   path('mostrar-horario/',mostrar_horario, name='mostrar_horario' ),
   path('saludo/<str:nombre>/<str:apellido>/', saludo, name='saludo')
   
   
   
   
   
   
   
    #path('saludo/<str:nombre>/<str:apellido>', views.saludo , name='saludo' ),
    #path('alumnos/', views.alumnos, name='alumnos'),
    #path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    #  path('Trompetas/', views.productos, name='Trompetas'),

 #   patgito/nuevo/<str:nombre>/<str:apellido>/<int:edad>/', crear_alumno, name='crear_alumno')

]

