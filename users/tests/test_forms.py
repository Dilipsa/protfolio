import time
from decimal import Decimal
from django.test import TestCase
from users.forms import ProfileUpdateForm
from users.models import User


class ProfileUpdateFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com')

    def test_form_fields(self):
        form = ProfileUpdateForm()
        form_fields = list(form.fields.keys())
        expected_fields = [
            'email',
            'home_address',
            'phone_number',
            'latitude',
            'longitude',
        ]
        self.assertCountEqual(form_fields, expected_fields)

    def test_form_validation(self):
        form_data = {
            'home_address': '123 Main St',
            'phone_number': '1234567890',
            'latitude': '37.12345',
            'longitude': '-122.98765',
        }
        form = ProfileUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_saving_data(self):
        form_data = {
            'home_address': '123 Main St',
            'phone_number': '1234567890',
            'latitude': Decimal('37.12345'),
            'longitude': Decimal('-122.98765'),
        }
        form = ProfileUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())
        saved_user = form.save()
        self.assertEqual(saved_user.home_address, form_data['home_address'])
        self.assertEqual(saved_user.phone_number, form_data['phone_number'])
        self.assertEqual(saved_user.latitude, form_data['latitude'])
        self.assertEqual(saved_user.longitude, form_data['longitude'])

    def test_form_readonly_email(self):
        form = ProfileUpdateForm(instance=self.user)
        email_field = form.fields['email']
        self.assertTrue(email_field.widget.attrs.get('readonly'))

    def test_form_error_handling(self):
        form_data = {
            'phone_number': '1234567890',
            'latitude': '37.12345',
            'longitude': '-122.98765',
        }
        form = ProfileUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('home_address', form.errors)

    def test_form_performance(self):
        num_iterations = 10000
        form_data = {
            'home_address': '123 Main St',
            'phone_number': '1234567890',
            'latitude': '37.12345',
            'longitude': '-122.98765',
        }

        start_time = time.time()
        for _ in range(num_iterations):
            form = ProfileUpdateForm(data=form_data)
            self.assertTrue(form.is_valid())
        end_time = time.time()

        elapsed_time = end_time - start_time
        average_time = elapsed_time / num_iterations

        print(f"Avg. Time per Iteration: {average_time} seconds")
