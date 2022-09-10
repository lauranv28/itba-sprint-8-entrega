from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    """Crear un nuevo usuario"""
    if request.method == 'POST':
        #Accede a la información enviada a través del form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #Guarda el usuario creado en la db
            form.save()
            username = form.cleaned_data['username']
            #Manda un mensaje al usuario de que su registro fue exitoso
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
        #Si se accede a esta ruta por un método get
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, "login/registration/register.html", context)


def login(request):
    return render(request, 'login/registration/login.html')


def homebanking(request):
    name = AuthUser.first_name
    return render(request, 'login/registration/homebanking.html')



