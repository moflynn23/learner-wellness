from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['speciality', 'therapist']

    SPECIALITY_CHOICES = [
        ('physical', 'Physical Wellness Appointment'),
        ('mental', 'Mental Health Appointment'),
    ]

    HOUR_CHOICES = [(str(hour), f"{hour}:00") for hour in range(8, 18)]  # Rnage can be adjusted
    time = forms.ChoiceField(choices=HOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))


    speciality = forms.ChoiceField(
        choices=SPECIALITY_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )


