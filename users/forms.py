from django import forms
from .models import User


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating user profile information.

    This form allows users to update their profile information, including home address,
    phone number, latitude, and longitude. The email field is readonly.
    """

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            field.required = True

    class Meta:
        model = User
        fields = (
            'email',
            'home_address',
            'phone_number',
            'latitude',
            'longitude'
        )
