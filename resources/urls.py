from django.urls import path
from .views import Resource, resources_view


urlpatterns = [
    path("", Resource.as_view(), name="resources"),
]