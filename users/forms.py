from django import forms
from .models import User

class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating user profile information.

    This form allows users to update their profile information, including home address,
    phone number, latitude, and longitude. The email field is disabled and cannot be edited.
    """
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = (
          'email', 
          'home_address', 
          'phone_number', 
          'latitude', 
          'longitude'
        )
