from django.shortcuts import render, redirect
from .models import Therapist, Booking
from .forms import BookingForm

def bookings(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = BookingForm()

    therapists = Therapist.objects.all()
    context = {'form': form, 'therapists': therapists}
    
    return render(request, 'bookings/bookings.html', context)


def booking_confirmation(request):
    return render(request, 'bookings/confirmation.html')