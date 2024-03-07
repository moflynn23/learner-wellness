from django.shortcuts import render
from django.views.generic import ListView
from .models import Session, Therapist
from .forms import BookingForm


class SessionListView(ListView):
    template_name = "bookings/bookings.html"
    model = Session
    context_object_name = "bookings"

def session(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = BookingForm()

    therapists = Therapist.objects.all()
    context = {'form': form, 'therapists': therapists}
    return render(request, 'bookings/bookings.html', context)