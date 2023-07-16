from django.urls import path  
from .views import (
  user_profile, 
  user_locations, 
  user_lists, 
  user_details,
  user_profile, 
  user_redirect_view
)

app_name='users'
urlpatterns = [
  path("~redirect/", view=user_redirect_view, name="redirect"),
  path("user-profile/", user_profile, name="user_profile"),
  path("user-details/<int:pk>/", user_details, name="user_details"),
  path("user-locations/", user_locations, name="user_locations"),
  path("user-lists/", user_lists, name="user_lists"),
]