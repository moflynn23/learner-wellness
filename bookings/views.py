from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Specialist, Booking
from django.views.generic import ListView


# Create your views here.

def bookings(request):
    form = BookingForm()
    specialists = Specialist.objects.values_list('user__username', flat=True)
    return render(request, 'bookings/bookings.html', {'form': form, 'specialists': specialists})


class Specialist(ListView):
    """View all user profiles"""
    template_name = "bookings/bookings.html"
    model = Specialist
    context_object_name = "specialists"

