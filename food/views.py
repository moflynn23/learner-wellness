from django.shortcuts import render
from django.views.generic import ListView

from .models import Restaurant

# Create your views here.
class UserRestaurant(ListView):
    """View all user profiles"""

    template_name = "food/food.html"
    model = Restaurant
    context_object_name = "restaurants"
    