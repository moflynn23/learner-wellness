from django.shortcuts import render
from django.views.generic import ListView
from .models import Resource

class Resource(ListView):
    """View all resources"""

    template_name = "resources/resources.html"
    model = Resource
    context_object_name = "resources"


