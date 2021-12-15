from rest_framework import viewsets

from .serializers import InventorySerializer, SupplierSerializer
from .models import Inventory, Supplier


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('name')
    serializer_class = InventorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer