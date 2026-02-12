from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import DailyConsumption

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )

    def test_login_valid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect to dashboard
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Stay on login page
        self.assertContains(response, 'Invalid credentials')

    def test_login_with_email(self):
        response = self.client.post(reverse('login'), {
            'username': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

class AddConsumptionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        self.client.login(username='testuser', password='password123')

    def test_add_consumption_get(self):
        response = self.client.get(reverse('add_consumption'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_consumption.html')
        self.assertContains(response, 'Add Daily Consumption')

    def test_add_consumption_post_valid(self):
        response = self.client.post(reverse('add_consumption'), {
            'food_item': 'Apple',
            'calories': 95,
            'quantity': 1
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        # Check if consumption was added
        consumption = DailyConsumption.objects.filter(user=self.user, food_item='Apple').first()
        self.assertIsNotNone(consumption)
        self.assertEqual(consumption.calories, 95)

    def test_add_consumption_post_invalid(self):
        response = self.client.post(reverse('add_consumption'), {
            'food_item': '',
            'calories': 'not_a_number',
            'quantity': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_consumption.html')
        # Check that no consumption was added
        self.assertEqual(DailyConsumption.objects.count(), 0)
