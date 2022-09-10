from rest_framework import serializers
from .models import Prestamos
from django.contrib.auth.models import User

#Endpoint préstamos
class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    prestamos = serializers.HyperlinkedRelatedField(many=True, view_name='pretamos/prestamos.html', read_only=True)
    class Meta:
        model = Prestamos
        #Hay que agregar el campo id de sucursal a los modelos
        fields = ['balance', 'customer_id']