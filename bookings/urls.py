from django.urls import path
from .views import bookings, booking_success_view  


urlpatterns = [
    path("", bookings, name="bookings"),
    path('booking-success/', booking_success_view, name='booking_success'),
   
]