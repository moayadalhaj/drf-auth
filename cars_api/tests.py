from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Car

class SnackModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user',password='pass')

        self.car = Car.objects.create(
            seller = self.user,
            car_name = 'Tesla',
            car_model = 'X',
            description = 'Electric car'
        )

    
    def test_Car_content(self):
        car = Car.objects.get(id=1)

        self.assertEqual(car.car_name, 'Tesla')
        self.assertEqual(car.car_model, 'X')
        self.assertEqual(car.description, 'Electric car')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('cars_list'))
        self.assertEqual(response.status_code, 200)
