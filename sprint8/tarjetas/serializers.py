from rest_framework import serializers
from .models import Tarjeta

#Endpoint tarjetas
class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    tarjeta = serializers.ReadOnlyField(source='customer_id.customer_id')
    class Meta:
        model = Tarjeta
        fields = '__all__'