from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    album_type = models.CharField(max_length=50)
    album_image = models.ImageField(upload_to='album_images/')