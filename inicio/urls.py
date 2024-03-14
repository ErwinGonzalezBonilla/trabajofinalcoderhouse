from django.urls import path
from inicio import views


from . import views

urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('mostrar-horario/',views.mostrar_horario, name='mostrar_horario' ),
    path('saludo/<str:nombre>/<str:apellido>', views.saludo , name='saludo' ),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('alumnos/nuevo/', views.crear_alumno, name='crear_alumno'),
    

 #   patgito/nuevo/<str:nombre>/<str:apellido>/<int:edad>/', crear_alumno, name='crear_alumno')

]
