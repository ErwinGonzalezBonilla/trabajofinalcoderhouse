from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def login(request):
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
           usuario= formulario.cleaned_data.get('username')
           contrasenia= formulario.cleaned_data.get('password')
        
           user = authenticate(username=usuario, password=contrasenia) 
           login(request, user)
           return redirect ('inicio')
       
           
    
    return render(request, 'usuario/login.html', {'formulario': formulario})
