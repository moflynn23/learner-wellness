from django.urls import path
from .views import bookings, book_specialist, booking_success_view

urlpatterns = [
    path("", bookings, name="bookings"),
    path('book-specialist/<int:specialist_id>/', book_specialist, name='book_specialist'),
    path('booking-success/', booking_success_view, name='booking_success'),
]

