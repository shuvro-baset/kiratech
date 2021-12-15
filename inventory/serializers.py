from rest_framework import serializers

from .models import Inventory, Supplier


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ('name',)


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inventory
        fields = ('name', 'description', 'note', 'stock', 'availability', 'supplier')
