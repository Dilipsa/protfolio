from django.test import TestCase
from django.urls import reverse, resolve
from users.views import (
    user_profile,
    user_locations,
    user_lists,
    user_details,
    user_redirect_view,
    check_email_registered,
)


class UsersURLTestCase(TestCase):
    def test_user_profile_url(self):
        url = reverse('users:user_profile')
        self.assertEqual(url, '/users/user-profile/')
        self.assertEqual(resolve(url).func, user_profile)

    def test_user_locations_url(self):
        url = reverse('users:user_locations')
        self.assertEqual(url, '/users/user-locations/')
        self.assertEqual(resolve(url).func, user_locations)

    def test_user_lists_url(self):
        url = reverse('users:user_lists')
        self.assertEqual(url, '/users/user-lists/')
        self.assertEqual(resolve(url).func, user_lists)

    def test_user_details_url(self):
        url = reverse('users:user_details', args=[1])  # Assuming the primary key is 1
        self.assertEqual(url, '/users/user-details/1/')
        self.assertEqual(resolve(url).func, user_details)

    def test_user_redirect_url(self):
        url = reverse('users:redirect')
        self.assertEqual(url, '/users/~redirect/')
        self.assertEqual(resolve(url).func, user_redirect_view)

    def test_check_email_registered_url(self):
        url = reverse('users:check_email_registered')
        self.assertEqual(url, '/users/check-email-registered/')
        self.assertEqual(resolve(url).func, check_email_registered)
