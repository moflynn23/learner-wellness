from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

TITLE_TYPES= ('physical', 'Physical Wellness Appointment'), ('mental', 'Mental Health Appointment'),

class Therapist(models.Model):
    """
    A model to create and manage user bookings
    """
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    
 
    def __str__(self):
        return self.client.username



class Session(models.Model):
    title = models.CharField(max_length=50, choices=TITLE_TYPES, null=False, blank=False)
    # ... (other fields)
    startTime = models.DateTimeField()
    therapist = models.ForeignKey(Therapist, related_name="sessions_as_therapist", on_delete=models.CASCADE, default=1)
    client = models.ForeignKey(User, related_name="bookings_client", on_delete=models.CASCADE)
    status = models.ForeignKey(User, related_name="bookings_status", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} - {self.startTime} - {self.therapist} - {self.client} - {self.status}"

