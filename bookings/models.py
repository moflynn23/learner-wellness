from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Therapist(models.Model):
    client = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    
 
    def __str__(self):
        return self.client.username

class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, default=1)
    startTime = models.DateTimeField()
    

    def __str__(self):
        return f"{self.client.username} - {self.therapist.client.username} - {self.startTime}"

