from rest_framework import serializers
from .models import Cuenta

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ['account_id', 'balance', 'tipos_de_cuentas_id']