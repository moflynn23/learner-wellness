from django.urls import path
from .views import Resource, resources_view, ResourcesDetail


urlpatterns = [
    path("", resources_view, name="resources"),
    path("resources/<slug:pk>/", ResourcesDetail.as_view(), name="video"),
    
]