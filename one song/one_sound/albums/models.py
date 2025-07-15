from django.db import models
from datetime import timedelta

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    album_type = models.CharField(max_length=50)
    album_image = models.ImageField(upload_to='album_images/')
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
