from django.urls import include, path
from rest_framework import routers
from . import views
app_name = 'inventory'
urlpatterns = [
    path('inventory', views.InventoryViewSet, name="inventory"),
]