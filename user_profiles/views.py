from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import UserProfile

# Create your views here.
class UserProfile(ListView):
    """View all user profiles"""

    template_name = "user_profiles/user_profiles.html"
    model = UserProfile
    context_object_name = "user_profiles"

class UserProfileDetail(DetailView):
    """View a single profile"""

    template_name = "user_profiles/profile_detail.html"
    model = UserProfile
    context_object_name = "user_profile"

