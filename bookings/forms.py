from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['speciality', 'date', 'time', 'specialist']

    SPECIALITY_CHOICES = [
        ('physical', 'Physical Wellness Appointment'),
        ('mental', 'Mental Health Appointment'),
    ]

    speciality = forms.ChoiceField(
        choices=SPECIALITY_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    date = forms.DateTimeField(
        widget=forms.widgets.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )

    HOUR_CHOICES = [(str(hour), f"{hour}:00") for hour in range(8, 18)]  # Adjust the range based on your availability
    time = forms.ChoiceField(choices=HOUR_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    specialist = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialist'].choices = []

    def clean(self):
        cleaned_data = super().clean()
        speciality = cleaned_data.get('speciality')

        if speciality:
            if speciality == 'physical':
                self.fields['specialist'].choices = [
                    ('Bob', 'Bob - Physical Wellness Specialist'),
                    ('Joe', 'Joe - Physical Wellness Specialist'),
                    ('Jill', 'Jill - Physical Wellness Specialist'),
                ]
            elif speciality == 'mental':
                self.fields['specialist'].choices = [
                    ('Bingus', 'Bingus - Mental Health Specialist'),
                    ('Sam', 'Sam - Mental Health Specialist'),
                    ('John', 'John - Mental Health Specialist'),
                ]

        return cleaned_data