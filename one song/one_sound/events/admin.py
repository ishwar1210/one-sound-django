from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'event_location', 'event_date', 'event_image']

admin.site.register(Event, EventAdmin)
