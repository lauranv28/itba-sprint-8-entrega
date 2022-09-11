from rest_framework import serializers
from .models import Cuentas

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuentas
        fields = ['account_id', 'balance', 'tipos_de_cuentas_id']