from django.shortcuts import render
from .models import Specialist, Booking
from .forms import BookingForm 


# Create your views here.


def bookings(request):
    return render(request, 'bookings/bookings.html')


# @login_required
def book_specialist(request, specialist_id):
    specialist = Specialist.objects.get(pk=specialist_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.specialist = specialist
            booking.save()
            return redirect('booking_success')  # Redirect to a success page
    else:
        form = BookingForm()

    return render(request, 'book_specialist.html', {'form': form, 'specialist': specialist})

def booking_success_view(request):
    return render(request, 'bookings/booking_success.html')