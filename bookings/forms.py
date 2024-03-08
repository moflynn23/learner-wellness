from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form to add a booking"""

    class Meta:
        model = Booking
        fields = [
            "user",
            "specialist",
            "date_time",
            "notes",
        ]

        notes = forms.CharField(widget=RichTextWidget())

        labels = {
            "user": "Booking By",
            "specialist": "Specialist",
            "date_time": "Booking Date/Time",
            "notes": "Notes",
        }
