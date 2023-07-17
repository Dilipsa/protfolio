from django.test import TestCase
from users.models import User


class UserModelTestCase(TestCase):
    def setUp(self):
        self.common_attrs = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password',
            'home_address': '123 Main St',
            'phone_number': '1234567890',
            'latitude': 37.12345,
            'longitude': -122.98765,
        }

    def test_user_creation(self):
        user = User.objects.create_user(**self.common_attrs)

        self.assertEqual(user.username, self.common_attrs['username'])
        self.assertEqual(user.email, self.common_attrs['email'])
        self.assertEqual(user.home_address, self.common_attrs['home_address'])
        self.assertEqual(user.phone_number, self.common_attrs['phone_number'])
        self.assertEqual(user.latitude, self.common_attrs['latitude'])
        self.assertEqual(user.longitude, self.common_attrs['longitude'])
        self.assertTrue(user.check_password(self.common_attrs['password']))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_superuser_creation(self):
        common_attrs = self.common_attrs.copy()
        common_attrs.update({
            'username': 'admin',
            'email': 'admin@example.com',
        })
        user = User.objects.create_superuser(**common_attrs)

        self.assertEqual(user.username, common_attrs['username'])
        self.assertEqual(user.email, common_attrs['email'])
        self.assertTrue(user.check_password(common_attrs['password']))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)
