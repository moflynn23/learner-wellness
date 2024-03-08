from django.urls import path
from .views import UserProfile, UserProfileDetail

urlpatterns = [
    path("", UserProfile.as_view(), name="user_profiles"),
    path("user_profiles/<slug:pk>/", UserProfileDetail.as_view(), name="profile_detail"),
]