from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField

# Choice Field
PROFILE_TYPES = (("instructor", "Instructor"), ("therapist", "Therapist"))

class UserProfile(models.Model):
    """
    A model to create and manage user profiles
    """

    user = models.ForeignKey(
        User, related_name="user_id", on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    about = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="user_profiles/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    profile_type = models.CharField(max_length=50, choices=PROFILE_TYPES, default="instructor")

    class Meta:
        ordering = ["-last_name"]

    def __str__(self):
        return str(self.first_name)