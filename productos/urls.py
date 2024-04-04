from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name= 'productos'

urlpatterns = [
    path("<int:id>/", views.detalle, name='detalle_producto'),
    
    ]
