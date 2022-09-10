from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.HyperlinkedModelSerializer(many=True, view_name='clientes/clientes.html', read_only=True)
    class Meta:
        model = Cliente
        fields = '__all__'

