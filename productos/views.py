from django.shortcuts import render
from .models import Product
# Create your views here.
def listado(request):
    productos = Product.objects.all()
    context= {'productos': productos}
    return render(request, "product_list.html", context)

def detalle(request, id):
    producto = Product.objects.filter(id = id).first()
    context= {'producto': producto}
    return render(request, "product_detail.html", context)