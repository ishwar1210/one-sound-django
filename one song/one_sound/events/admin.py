from django.contrib import admin
from .models import Event, EventDetail

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'event_location', 'event_date', 'event_image']

class EventDetailAdmin(admin.ModelAdmin):
    list_display = ['event',  'event_duration', 'event_language', 'event_age_limit', 'event_genres', 'event_time', 'event_about']


admin.site.register(Event, EventAdmin)
admin.site.register(EventDetail, EventDetailAdmin)
