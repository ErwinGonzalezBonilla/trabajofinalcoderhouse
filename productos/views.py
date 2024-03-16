from django.shortcuts import render

# Create your views here.
def listado(request):
    return render(request, "product_list.html")