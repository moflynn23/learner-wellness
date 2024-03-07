from django.urls import path
from .views import Resource


urlpatterns = [
    path("", Resource.as_view(), name="resources"),
]