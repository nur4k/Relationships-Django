from django.shortcuts import render
from .models import SalesOrders
from .serializers import OrderSerializer
from rest_framework.viewsets import ModelViewSet


def info(request):
    return render(request, 'index.html', {'orders': SalesOrders.objects.all()})

class OrderView(ModelViewSet):
    queryset = SalesOrders.objects.all()
    serializer_class = OrderSerializer
