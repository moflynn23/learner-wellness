from django.urls import path
from .views import Restaurant


urlpatterns = [
    path("", Restaurant.as_view(), name="food"),
    
]


