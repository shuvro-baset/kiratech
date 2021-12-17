from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'inventory'
urlpatterns = [
    path('inventory', views.InventoryViewSet.as_view({'get': 'list'}), name="inventory"),
    path('inventory/<int:id>/', views.SingleInventoryViewSet.as_view({'get': 'retrieve'}), name="single_inventory"),
    path('create-inventory', views.CreateInventoryViewSet.as_view({'post': 'create'}), name="create-inventory"),
]
