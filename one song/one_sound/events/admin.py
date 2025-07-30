from django.contrib import admin
from .models import Booking, Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','event_name', 'event_date', 'start_time', 'duration', 'venue', 'description', 'event_image', 'cover_image', 'price', 'age_restriction', 'language', 'category', 'organizer_logo', 'artists_names', 'artists_images']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'event', 'user', 'date', 'qty', 'payment_id']

admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)


