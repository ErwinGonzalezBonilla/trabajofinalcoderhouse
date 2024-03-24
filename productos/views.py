from django.shortcuts import render
from .models import Product
# Create your views here.
def listado(request):
    queryDictionary = request.GET
    tipo = queryDictionary.get('tipo', '')
    if tipo == '':
        productos = Product.objects.all()
    else:
        productos = Product.objects.filter(tipo__exact=tipo)
    context= {'productos': productos}
    return render(request, "product_list.html", context)

def detalle(request, id):
    producto = Product.objects.filter(id = id).first()
    context= {'producto': producto}
    return render(request, "product_detail.html", context)