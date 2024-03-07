from django.shortcuts import render
from django.views.generic import ListView
from .models import Resource

class Resource(ListView):
    """View all resources"""

    template_name = "resources/resources.html"
    model = Resource
    context_object_name = "resources"

def resources_view(request):
    video_resources = Resource.objects.filter(resource_type='video')
    podcast_resources = Resource.objects.filter(resource_type='podcast')
    article_resources = Resource.objects.filter(resource_type='article')

    context = {
        'video_resources': video_resources,
        'podcast_resources': podcast_resources,
        'article_resources': article_resources,
    }

    return render(request, 'resources/resources.html', context)

    