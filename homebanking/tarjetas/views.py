from django.shortcuts import render
from tarjetas.models import Tarjeta, TarjetaSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
# Create your views here.


def tarjetas(request):
    return render(request, "tarjetas/tarjetas.html")


class TarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TarjetaSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'customer_id'

    def get_queryset(self):
        id = self.kwargs['id']
        return Tarjeta.objects.filter(customer_id=id)
