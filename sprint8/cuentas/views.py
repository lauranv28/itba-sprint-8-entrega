from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from clientes.models import Cliente
from .models import Cuenta
from .serializers import CuentaSerializer

# Create your views here.
@login_required(login_url='login/')
def cuentas(request):
    try:
        datoscuenta = Cuenta.objects.filter(customer_id=datoscuenta.customer_id)
    except:
        datoscuenta = None
    return render(request, "cuentas/cuentas.html", {'datoscuenta': datoscuenta})

class CuentaViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer = CuentaSerializer
    def get_queryset(self):
        id = self.request.user.id
        user = Cliente.objects.filter(user=id)
        try:
            user_id = user[0].customer_id
            return Cuenta.objects.filter(customer_id=user_id)
        except:
            cuenta = []
            return cuenta