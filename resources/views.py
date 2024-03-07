from django.shortcuts import render
from django.views.generic import ListView
from .models import Resource

class Resource(ListView):
    
    """View all resources"""
    template_name = "resources/resources.html"
    model = Resource
    context_object_name = "resources"

def resources_view(request):

    """Filter resources"""
    mydata1 = Resource.objects.filter(resource_type='videos')
    mydata2 = Resource.objects.filter(resource_type='podcasts')
    mydata3 = Resource.objects.filter(resource_type='articles')

    context = {
        'video_resources': mydata1,
        'podcast_resources': mydata2,
        'article_resources': mydata3,
    }

    return render(request, 'resources/resources.html', context)

    