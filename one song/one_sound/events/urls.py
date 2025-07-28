from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.events, name='events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('send-booking-email/', views.send_booking_email, name='send_booking_email'),
]