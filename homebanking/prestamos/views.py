from xmlrpc.client import boolean
from django.shortcuts import render
from .forms import FormularioPrestamo
from clientes.models import Cliente, TipoCliente
from .models import Prestamos
from cuentas.models import Cuenta

# Create your views here.
def prestamos(request):
    prestamos_form = FormularioPrestamo
    if request.method == 'POST':
        if prestamos_form.is_valid():
            prestamos_form.save()
            name = request.POST.get('name')
            email = request.POST.get('email')
            monto = request.POST.get('monto')
            tipo_prestamo = request.POST.get('tipo_prestamo')
            fecha_inicio = request.POST.get('fecha_inicio')
            for customer_id in Cliente:
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
                        return (Prestamos.loan_type==monto, Prestamos.loan_date==fecha_inicio, Prestamos.loan_type==tipo_prestamo, Cuenta.balance + monto, print('APROBADO'))
    return render(request,"prestamos/prestamos.html", {'form': prestamos_form})