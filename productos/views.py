from django.shortcuts import render
from .models import Product
# Create your views here.
def listado(request):
    productos = Product.objects.all()
    context= {'productos': productos}
    return render(request, "product_list.html", context)