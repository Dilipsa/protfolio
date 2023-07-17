from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from users.models import User


class TestUserCreation(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_creation(self):
        url = reverse('account_signup')
        email = 'test@example.com'
        data = {
            'email': email,
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        # Check if the user is created and can log in
        self.assertEqual(User.objects.filter(email=email).count(), 1)
        self.assertTrue(self.client.login(email=email, password='testpassword'))


class TestUserLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='password'
        )

    def test_user_login(self):
        login_url = reverse('account_login')
        data = {
            'login': 'test@example.com',
            'password': 'password',
        }
        response = self.client.post(login_url, data, follow=True)
        self.assertEqual(response.status_code, 200)  # Expecting successful login
        redirect_url = response.redirect_chain[-1][0]  # Get the last redirect URL in the chain
        if redirect_url == reverse('users:user_lists'):
            # User is a superuser
            response = self.client.get(redirect_url)
            self.assertEqual(response.status_code, 200)  # Successful login
        else:
            # User is not a superuser
            self.assertEqual(redirect_url, reverse('users:user_profile'))


class TestUserProfileView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')

    def test_profile_update(self):
        url = reverse('users:user_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_profile.html')

        data = {
            'home_address': '123 Main St',
            'phone_number': '1234567890',
            'latitude': 37.12345,
            'longitude': -122.98765
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:user_profile'))

        self.user.refresh_from_db()
        self.assertEqual(self.user.home_address, '123 Main St')
        self.assertEqual(self.user.phone_number, '1234567890')
        self.assertEqual(self.user.latitude, Decimal('37.12345'))  # Convert the floating-point number to Decimal
        self.assertEqual(self.user.longitude, Decimal('-122.98765'))  # Convert the floating-point number to Decimal

    def test_profile_update_invalid_form(self):
        url = reverse('users:user_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_profile.html')

        data = {}  # Empty data should result in an invalid form
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_profile.html')
        self.assertFormError(response, 'form', 'home_address', 'This field is required.')


class TestUserListView(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='password')
        self.client = Client()
        self.client.login(username='admin', password='password')

    def test_user_lists_view(self):
        url = reverse('users:user_lists')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_lists.html')


class TestUserLocationsView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.superuser = User.objects.create_superuser(username='admin', email='admin@example.com', password='password')
        self.client = Client()
        self.client.login(username='admin', password='password')

    def test_user_locations_view(self):
        url = reverse('users:user_locations')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(len(response.json()), 2)  # Assuming two users are created, including the superuser


class TestCheckEmailRegisteredView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.client = Client()

    def test_check_email_registered_view(self):
        url = reverse('users:check_email_registered')
        response = self.client.get(url, {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), {'registered': True})

        response = self.client.get(url, {'email': 'other@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json(), {'registered': False})
