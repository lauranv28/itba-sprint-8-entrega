from rest_framework import serializers
from .models import Tarjeta
from django.contrib.auth.models import User

#Endpoint tarjetas
class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    tarjeta = serializers.HyperlinkedRelatedField(many=True, view_name='tarjetas/tarjetas.html', read_only=True)
    class Meta:
        model = Tarjeta
        fields = '__all__'