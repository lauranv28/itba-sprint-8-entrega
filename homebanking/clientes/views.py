from http.client import HTTPResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

# Create your views here.


@login_required(login_url='login/')
def cliente(request):
    try:
        datoscliente = Cliente.objects.get(user_id=request.user.id)
    except:
        datoscliente = None

    return render(request, 'clientes/clientes.html', {'datoscliente': datoscliente})


class ClienteViewSet(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrievemodelMixin, viewsets.GenericViewSet):

    serializer = ClienteSerializer

    def get_queryset(self):
        id = self.request.user.id
        return Cliente.objects.filter(user=id)
