from django.contrib import admin
from .models import Album

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'album_name', 'album_type', 'album_image']
   

admin.site.register(Album, AlbumAdmin)