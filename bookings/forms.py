from django import forms
from .models import Session, Therapist, User

class BookingForm(forms.ModelForm):
    TITLE_CHOICES = [
        ('physical', 'Physical Wellness Appointment'),
        ('mental', 'Mental Health Appointment'),
    ]

    HOUR_CHOICES = [(str(hour), f"{hour}:00") for hour in range(8, 18)]  # Range can be adjusted
    time = forms.ChoiceField(choices=HOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    title = forms.ChoiceField(choices=TITLE_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    startTime = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control datetimepicker'}))

    therapist = forms.ModelChoiceField(queryset=Therapist.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    client = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    status = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Session
        fields = ['title', 'startTime', 'time', 'therapist', 'client', 'status']

    
    