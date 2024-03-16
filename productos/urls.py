from django.urls import path
from . import views

app_name= 'productos'

urlpatterns = [
    path("<int:id>/", views.detalle, name='detalle_producto'),
    path("", views.listado)
]
