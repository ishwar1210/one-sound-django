from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_location = models.CharField(max_length=100)
    event_date = models.DateField()
    event_image = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.event_name
    
class EventDetail(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    detail_text = models.TextField()
    event_duration = models.DurationField()
    event_language = models.CharField(max_length=50, default='Hindi')
    event_age_limit = models.PositiveIntegerField(default=0)
    event_genres = models.CharField(max_length=100, default='General')

    def __str__(self):
        return f"Detail for {self.event.event_name}"