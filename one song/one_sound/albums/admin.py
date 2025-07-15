from django.contrib import admin
from .models import Album, Song


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'album_name', 'album_type', 'album_image']
   

admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'album', 'song_name', 'audio_file', 'movie_name', 'duration']
    list_filter = ['album']
    search_fields = ['song_name']

admin.site.register(Song, SongAdmin)