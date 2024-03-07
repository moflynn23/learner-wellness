from django.shortcuts import render, redirect
from .models import Specialist, Booking
from .forms import BookingForm

# Create your views here.

def bookings(request):
    form = BookingForm()
    specialists = Specialist.objects.values_list('user__username', flat=True)
    return render(request, 'bookings/bookings.html', {'form': form, 'specialists': specialists})

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
        
    therapists = Therapist.objects.all()
    context = {'form': form, 'therapists': therapists}
    return render(request, 'bookings/bookings.html', context)

#class UserProfile(ListView):
    #"""View all user profiles"""

 #   template_name = "user_profiles/user_profiles.html"
  #  model = UserProfile
   # context_object_name = "user_profiles"

    
    #   return render(request, 'book_specialist.html', {'form': form, 'specialist': specialist})

#def booking_success_view(request):
 #   return render(request, 'bookings/booking_success.html')
