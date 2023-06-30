from django.test import TestCase
from django.urls import reverse
from Restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu model
        Menu.objects.create(name='Menu 1', price=10.99)
        Menu.objects.create(name='Menu 2', price=15.99)
        Menu.objects.create(name='Menu 3', price=12.50)

    def test_getall(self):
        # Initialize API client
        client = APIClient()

        # Make GET request to retrieve all Menu objects
        url = reverse('menu-list')
        response = client.get(url, format='json')

        # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve serialized data from the response
        serialized_data = response.data

        # Get all Menu objects from the database
        menus = Menu.objects.all()

        # Serialize the Menu objects
        expected_data = []
        for menu in menus:
            expected_data.append({
                'name': menu.name,
                'price': str(menu.price)
            })

        # Check if the serialized data matches the expected data
        self.assertEqual(serialized_data, expected_data)
