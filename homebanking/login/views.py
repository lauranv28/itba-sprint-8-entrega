from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *
from empleados.models import Empleado
from clientes.models import Cliente

# Create your views here.


def register(request):
    """Crear un nuevo usuario"""
    if request.method == 'POST':
        context = {'form': form}
        #Accede a la información enviada a través del form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #Determinar si es cliente o empleado
            coe = form.cleaned_data.get('coe')
            dni = form.cleaned_data.get('dni')

            if coe == 'Cliente':
                try:
                    newuser = Cliente.objects.get(customer_DNI = dni)
                    if newuser.user is None:
                        user = form.save()
                        newuser.user = user
                        #Guarda el usuario creado en la db
                        newuser.save()
                    else:
                        messages.error(request, 'Usuario existente')
                        return render(request, "login/registration/register.html", context)
                except:
                    messages.error(request, 'DNI inexistente en base de datos')
                    return render(request, "login/registration/register.html", context)
                return redirect('login')
            elif coe == 'Empleado':
                try:
                    newuser = Empleado.objects.get(employee_dni = dni)
                    if newuser.user is None:
                        user = form.saveuser()
                        user.is_staff = True
                        user.save()
                        newuser.user = user
                        #Guarda el usuario creado en la db
                        newuser.save()
                    else:
                        messages.error(request, 'Usuario existente')
                        return render(request, "login/registration/register.html", context)
                except:
                    messages.error(request, 'DNI inexistente en base de datos')
                    return render(request, "login/registration/register.html", context)
                return redirect('login')
    #Si se accede a esta ruta por un método get
    else:
        form = UserRegisterForm()
    return render(request, "login/registration/register.html", context)


def login(request):
    return render(request, 'login/registration/login.html')


def homebanking(request):
    name = AuthUser.first_name
    return render(request, 'login/registration/homebanking.html')
