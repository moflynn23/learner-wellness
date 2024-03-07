from django.db import models

# Create your models here.

# each model is represented by a class that subclasses django.db.models.Model.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    restaurant_menu = models.CharField(max_length=1000)
#    image = CloudinaryField('image', default='placeholder')  
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.restaurant_name
