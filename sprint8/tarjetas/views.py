from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .models import Tarjeta, MarcasDeTarjetas
from .serializers import TarjetaSerializer
from clientes.views import cliente

# Create your views here.
@login_required(login_url='login/')
def tarjetas(request):
    try:
        datatarjeta = Tarjeta.objects.filter(customer_id = cliente.datoscliente.customer_id)
    except:
        datatarjeta = None

    try:
        datamarca = MarcasDeTarjetas.objects.filter(card_brand_id = datatarjeta.marcas_tarjeta_id)
    except:
        datamarca = None
    
    context = {'datatarjeta': datatarjeta, 'datamarca': datamarca}
    return render(request,"tarjetas/tarjetas.html", context)


class TarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class= TarjetaSerializer
    permission_classes= [IsAdminUser]
    lookup_field = 'customer_id'
    def get_queryset(self):
        id = self.kwargs['id']
        return Tarjeta.objects.filter(customer_id = id)