from xmlrpc.client import boolean
from django.shortcuts import render
from django.contrib import messages
from .forms import FormularioPrestamo
from clientes.models import Cliente, TipoCliente
from .models import Prestamos
from cuentas.models import Cuenta

# Create your views here.
def prestamos(request):
    prestamos_form = FormularioPrestamo()
    if request.method == 'POST':
        if prestamos_form.is_valid():
            prestamos_form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            monto = request.POST.get('monto')
            dni = request.POST.get('dni')
            tipo_prestamo = request.POST.get('tipo_prestamo')
            fecha_inicio = request.POST.get('fecha_inicio')
            balance = Cuenta.balance

            #Filtrar por cliente
            filter_cliente_b = TipoCliente.object.filter(tipos_de_clientes='BLACK').order_by('username')
            filter_cliente_g = TipoCliente.object.filter(tipos_de_clientes='GOLD').order_by('username')
            filter_cliente_c = TipoCliente.object.filter(tipos_de_clientes='CLASSIC').order_by('username')

            if dni in filter_cliente_b:
                if monto <= 500000:
                    messages.success(request, 'Préstamo aprobado')
                    prestamo = Prestamos(loan_total=monto, loan_date=fecha_inicio, loan_type=tipo_prestamo)
                    prestamo.save()
                    #Actualiza el saldo de cuenta
                    balance += monto
                    balance.save()
                else:
                    messages.success(request, 'Préstamo desaprobado, el monto requerido supera el habilitado')
            elif dni in filter_cliente_g:    
                if monto <= 300000:
                    messages.success(request, 'Préstamo aprobado')
                    prestamo = Prestamos(loan_total=monto, loan_date=fecha_inicio, loan_type=tipo_prestamo)
                    prestamo.save()
                    #Actualiza el saldo de cuenta
                    balance += monto
                    balance.save()
                else:
                    messages.success(request, 'Préstamo desaprobado, el monto requerido supera el habilitado')
            elif dni in filter_cliente_c:
                if monto <= 100000:
                    messages.success(request, 'Préstamo aprobado')
                    prestamo = Prestamos(loan_total=monto, loan_date=fecha_inicio, loan_type=tipo_prestamo)
                    prestamo.save()
                    #Actualiza el saldo de cuenta
                    balance += monto
                    balance.save()
                else:
                    messages.success(request, 'Préstamo desaprobado, el monto requerido supera el habilitado')
            
            
            

            """ for customer_id in Cliente:
                if TipoCliente == 'BLACK':
                    monto_limite = 500000 
                    if monto <= 500000:
                        return (Prestamos.loan_type==monto, Prestamos.loan_date==fecha_inicio, Prestamos.loan_type==tipo_prestamo,Cuenta.balance + monto, print('APROBADO'))
                elif TipoCliente == 'GOLD':
                    monto_limite = 300000
                    if monto <= 300000:
                        return (Prestamos.loan_type==monto, Prestamos.loan_date==fecha_inicio, Prestamos.loan_type==tipo_prestamo, Cuenta.balance + monto, print('APROBADO'))
                elif TipoCliente == 'CLASSIC':
                    monto_limite = 100000
                    if monto <= monto_limite:
                        return (Prestamos.loan_type==monto, Prestamos.loan_date==fecha_inicio, Prestamos.loan_type==tipo_prestamo, Cuenta.balance + monto, print('APROBADO')) """
    return render(request,"prestamos/prestamos.html", {'form': prestamos_form})