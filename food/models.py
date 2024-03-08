from django.db import models
from django_resized import ResizedImageField
from djrichtextfield.models import RichTextField


# Create your models here.

# each model is represented by a class that subclasses django.db.models.Model.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    restaurant_menu = RichTextField(max_length=10000, null=False, blank=False)
    pub_date = models.DateTimeField("date published")
    slug = models.SlugField(max_length=200, unique=True, default=0)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="food/",
        force_format="WEBP",
        default='static/images/nobody.nobody.jpg'
    )

    def __str__(self):
        return self.restaurant_name