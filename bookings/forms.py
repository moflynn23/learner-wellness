from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    SPECIALIST_CHOICES = [
        ('physical', 'Physical Wellness Appointment'),
        ('mental', 'Mental Health Appointment'),
    ]

    specialist_type = forms.ChoiceField(
        choices=SPECIALIST_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Booking
        fields = ['specialist_type', 'date_time', ]