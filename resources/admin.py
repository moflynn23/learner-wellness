from django.contrib import admin
from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
        "body",
        "resource_type"
    )

    list_filter = ("resource_type",)

