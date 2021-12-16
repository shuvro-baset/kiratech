from rest_framework import serializers

from .models import Inventory, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    # supplier = serializers.SerializerMethodField()
    class Meta:
        model = Inventory
        fields = ('name', 'description', 'note', 'stock', 'availability', 'supplier')

    # def get_supplier(self, obj):
    #     return obj.supplier if obj.supplier else []
