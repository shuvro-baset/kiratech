from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Inventory)

class InvntoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'note', 'stock', 'availability', 'supplier']