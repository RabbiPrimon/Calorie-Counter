from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

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
