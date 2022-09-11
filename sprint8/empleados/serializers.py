from rest_framework import serializers
from .models import Sucursal
from prestamos.models import Prestamos

class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamos
        fields = '__all__'


class ListaSucursalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['branch_number', 'branch_name']
        read_only_fields = ['brach_id', 'branch_address_id']
