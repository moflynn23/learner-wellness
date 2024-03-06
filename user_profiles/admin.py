from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "profile_type",
        "about",
        "image",
    )
    list_filter = ("profile_type",)