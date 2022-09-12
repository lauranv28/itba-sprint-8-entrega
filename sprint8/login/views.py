from selectors import DefaultSelector
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from empleados.models import Empleado
from clientes.models import Cliente
from empleados.models import Sucursal

# Create your views here.
def register(request):
    '''Crear un nuevo usuario'''
    if request.method == 'POST':
        
        #Accede a la información enviada a través del form
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            #Determinar si es cliente o empleado
            coe = form.cleaned_data.get('coe')
            dni = form.cleaned_data.get('dni')
            #username = User.objects.get('username')
            #suc_id = Sucursal.objects.get('branch_id')
            
            if coe == 'Cliente':
                try:
                    newuser = Cliente.objects.get(customer_DNI = dni)
                    if newuser.username is None:
                        username = form.save()
                        newuser.username = username
                        #Guarda el usuario creado en la db
                        newuser.save()
                        
                        """ Al migrar dice que branch_id del cliente es nulo y por defecto 
                        tiene not null, no sé bien qué es lo que está mal """
                        #Le asigna una sucursal
                        #newuser = Cliente.objects.get(branch_id = suc_id)
                        #newuser.save()
                        # Manda un mensaje al usuario de que su registro fue exitoso
                        messages.success(request, 'Usuario creado')
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
                    if newuser.username is None:
                        username = form.saveuser()
                        username.is_staff = True
                        username.save()
                        newuser.username = username
                        #Guarda el usuario creado en la db
                        newuser.save()
                        # Manda un mensaje al usuario de que su registro fue exitoso
                        messages.success(request, 'Usuario creado')
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
    context = {'form':form}
    return render(request, "login/registration/register.html", context)


def login(request):
    return render(request, 'login/registration/login.html')


def homebanking(request):
    return render(request, 'login/registration/homebanking.html')
