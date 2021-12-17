# import json
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from inventory.serializers import InventorySerializer
# from inventory.models import Inventory, Supplier
#
# #
# # class CreateInventoryViewSetTestCase(APITestCase):
# #
# #     def test_create_inventory(self):
# #         data = {
# #             "name": "forhad pharmacy",
# #             "description": "description",
# #             "note": "note",
# #             "stock": 10,
# #             "availability": 1,
# #             "supplier": [3]
# #         }
# #         response = self.client.post("api/create-inventory", data)
# #         print(response, data)
# #         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
# class InventoryViewSetTestCase(APITestCase):
#     # list_url = reverse("inventory")
#     data = Inventory.objects.all()
#     def inventory_list(self):
#         response = self.client.get("api/inventory", data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('inventory.urls')),
    ]

    def test_create_inventory(self):

        url = "api/inventory"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)