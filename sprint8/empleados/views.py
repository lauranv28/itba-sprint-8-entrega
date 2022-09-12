from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SucursalSerializer, ListaSucursalesSerializer
from .models import Sucursal
from clientes.models import Cliente
from prestamos.models import Prestamos

# Create your views here.
class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SucursalSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        client_list = Cliente.objects.filter(branch_id = id)
        list = []
        loans = Prestamos.objects.all()
        for l in loans:
            for c in client_list:
                if l.customer_id == c.customer_id:
                    list.append(l)
        return list

class PublicEndpoint(APIView):
    permission_classes = []

    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = ListaSucursalesSerializer(sucursales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)