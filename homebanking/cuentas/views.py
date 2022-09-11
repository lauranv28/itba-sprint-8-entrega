from django.shortcuts import render
from .models import Cliente
from cuentas.models import Cuenta
from .serializers import CuentaSerializer
from rest_framework import viewsets
# Create your views here.


def cuentas(request):
    cuentas = Cuenta.objects.all()
    return render(request, "cuentas/cuentas.html", {'cuentas': cuentas})


class CuentaViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer = CuentaSerializer

    def get_queryset(self):
        id = self.request.user.id
        user = Cliente.objects.filter(user=id)
        try:
            us_id = user[0].customer_id
            return Cuenta.objects.filter(customer_id=us_id)
        except:
            acc = []
            return acc
