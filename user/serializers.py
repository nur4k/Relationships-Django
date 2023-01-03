from .models import SalesOrders
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrders
        fields = '__all__'