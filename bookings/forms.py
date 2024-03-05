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

    
    date = forms.DateTimeField(
        widget=forms.widgets.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )

    HOUR_CHOICES = [(str(hour), f"{hour}:00") for hour in range(8, 18)]  # Adjust the range based on your availability
    time = forms.ChoiceField(choices=HOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Booking
        fields = ['specialist_type', 'date', 'time' ]

