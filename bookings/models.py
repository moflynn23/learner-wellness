from django.db import models
from django.contrib.auth.models import User

class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # Add other specialist fields

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    notes = models.TextField(blank=True)
    # Add other booking fields

    def __str__(self):
        return f"{self.user.username} - {self.specialist.user.username} - {self.date_time}"