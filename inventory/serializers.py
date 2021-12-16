from rest_framework import serializers

from .models import Inventory, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields ='__all__'
