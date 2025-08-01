from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    venue = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(default="No description available")
    event_image = models.ImageField(upload_to='events/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='events/covers/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age_restriction = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=100, blank=True)
    organizer_logo = models.ImageField(upload_to='events/logos/', blank=True, null=True)
    artists_names = models.CharField(max_length=255, blank=True, null=True)
    artists_images = models.ImageField(upload_to='events/artists/', blank=True, null=True)
    
    def __str__(self):
        return self.event_name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.event.event_name}"

