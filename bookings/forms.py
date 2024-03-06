from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['therapist', 'startTime']

startTime = forms.DateTimeField(
        widget=forms.widgets.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )   