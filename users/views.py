from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from django.contrib import messages
from django.views.generic import RedirectView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from .forms import ProfileUpdateForm
from .models import User
from .functions import allow_access_to_superuser

class UserProfileView(LoginRequiredMixin, UpdateView):
    """
    View for updating user profile.

    This view allows authenticated users to update their profile information.
    It uses the 'ProfileUpdateForm' form to display and handle the form submission.

    Attributes:
        model (Model): The user model class.
        form_class (Form): The form class to use for the user profile update.
        template_name (str): The template name to render the user profile update form.
    """
    model = User
    form_class = ProfileUpdateForm
    template_name = 'users/user_profile.html'
    success_url = reverse_lazy('users:user_details')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Profile updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Update failed. Please check the form entries.")
        return super().form_invalid(form)
        

user_profile = UserProfileView.as_view()

class UserDetailsView(DetailView):
    """
    View for rendering the user details page.

    This view retrieves the user object with the given primary key (pk) and renders the user details page.
    If the user is not found, a 404 page is displayed.

    Attributes:
        model (Model): The user model class.
        template_name (str): The template name to render the user details page.
        context_object_name (str): The name of the variable to use in the template for the user object.
    """

    model = User
    template_name = 'users/user_details.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        """
        Retrieve the user object based on the primary key (pk).

        If the user is not found, a 404 page is displayed.

        Returns:
            User: The user object.

        Raises:
            Http404: If the user with the given primary key does not exist.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, pk=pk)

user_details = UserDetailsView.as_view()

@allow_access_to_superuser
def user_lists(request):
    """
    Render the user lists page.

    This view is only accessible to superusers.
    """
    return render(request, 'users/user_lists.html')

@allow_access_to_superuser
def user_locations(request):
    """
    Retrieve the locations of all users and return them as JSON.

    Retrieve all user objects from the database and create a list of dictionaries containing user location details.
    Each dictionary represents a user and includes their id, username, email, home address, phone number, latitude, and longitude.

    Returns:
        JsonResponse: JSON response containing the user locations.

    """
    users = User.objects.all()
    locations = [
        {   
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'home_address': user.home_address if user.home_address else None,
            'phone_number': user.phone_number  if user.home_address else None,
            'latitude': user.latitude  if user.latitude else None,
            'longitude': user.longitude  if user.longitude else None
        }
        for user in users
    ]
    return JsonResponse(locations, safe=False)

class UserRedirectView(LoginRequiredMixin, RedirectView):
    """
    Redirect the user to a specific URL based on their user type.

    If the user is a superuser, redirect them to the 'users:user_lists' URL.
    Otherwise, redirect them to the 'users:user_profile' URL.

    Returns:
        str: The URL to redirect the user to.

    """
    permanent = False
    query_string = True
    pattern_name = 'user_profile'

    def get_redirect_url(self):
        if self.request.user.is_superuser:
            next_url = 'users:user_lists'
        else:
            next_url = 'users:user_profile'

        return reverse(next_url)

user_redirect_view = UserRedirectView.as_view()
