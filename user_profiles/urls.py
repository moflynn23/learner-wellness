from django.urls import path
from .views import UserProfiles, UserProfileDetail

urlpatterns = [
    path("", UserProfiles.as_view(), name="user_profiles"),
    path("user_profiles/<slug:pk>/", UserProfileDetail.as_view(), name="profile_detail"),
]