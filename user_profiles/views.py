from django.shortcuts import render
from django.views.generic import ListView

from .models import UserProfile

# Create your views here.
class UserProfile(ListView):
    """View all user profiles"""

    template_name = "user_profiles/user_profiles.html"
    model = UserProfile
    context_object_name = "user_profiles"