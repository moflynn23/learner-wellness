from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.db import models

# Choice Field
RESOURCE_TYPES = (("physical activities", "Physical Activities"), ("therapy", "Therapy"))

class Resource(models.Model):
   
    title = models.CharField(max_length=200)
    body = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="resources/",
        force_format="WEBP",
        blank=False,
        null=False,
    )

    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPES, default="therapy")

def __str__(self):
    return self.title

