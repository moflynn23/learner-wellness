from django.urls import path
from .views import bookings, booking_confirmation


urlpatterns = [
    path("", bookings, name="bookings"),
    path('booking-comfirmation/', booking_confirmation, name='booking_confirmation'),

]