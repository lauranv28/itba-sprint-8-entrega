from rest_framework import serializers
from .models import Prestamos

#Endpoint préstamos
class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamos
        fields = '__all__'