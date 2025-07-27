from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Album(models.Model):
    # Add these fields:
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Your existing fields
    album_name = models.CharField(max_length=100)
    album_type = models.CharField(max_length=100)
    album_image = models.ImageField(upload_to='albums/')
    cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)

    def __str__(self):
        return self.album_name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_image = models.ImageField(upload_to='song_images/', blank=True, null=True)
    song_name = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    movie_name = models.CharField(max_length=200, default='', blank=True)
    duration = models.DurationField(default=timedelta(minutes=3))
    
    def __str__(self):
        return self.song_name

class FeaturedAlbum(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    position = models.IntegerField(default=1, help_text="Position in slider (1 or 2)")
    custom_heading = models.CharField(max_length=200, blank=True, help_text="Leave blank to use album name")
    custom_subheading = models.CharField(max_length=200, blank=True)
    slide_image = models.ImageField(upload_to='featured_slides/', blank=True, null=True) 
    
    class Meta:
        ordering = ['position']
    
    def __str__(self):
        return f"Featured: {self.album.album_name} (Position {self.position})"

class WeeksTop(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1)

class NewHit(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1)

class PopularAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=1)
