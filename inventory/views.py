from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .serializers import InventorySerializer, SupplierSerializer
from .models import Inventory, Supplier
from rest_framework import parsers, renderers, status, viewsets


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('name')
    serializer_class = InventorySerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer


class SingleInventoryViewSet(ViewSet):
    queryset = Inventory.objects.all()

    # serializer_class = InventorySerializer

    def retrieve(self, request, id, format=None):

        inventory_ins = Inventory.objects.filter(pk=id).first()
        print(inventory_ins)
        if inventory_ins:
            serializer = InventorySerializer(inventory_ins, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateInventoryViewSet(ViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def create(self, request, format=None):

        serializer = InventorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
