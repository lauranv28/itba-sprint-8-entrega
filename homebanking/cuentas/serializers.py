from rest_framework import serializers
from .models import Cuentas
from django.contrib.auth.models import User

class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    cuenta = serializers.HyperlinkedRelatedField(many=True, view_name='cuentas/cuentas.html', read_only=True)
    class Meta:
        model = Cuenta
        fields = ['balance', 'tipos_de_cuentas_id']