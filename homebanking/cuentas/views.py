from django.shortcuts import render

from cuentas.models import Cuenta

# Create your views here.
def cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request,"cuentas/cuentas.html", {'cuentas':cuentas})