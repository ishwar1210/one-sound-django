from django.contrib import admin
from .models import Album, WeeksTop, NewHit, PopularAlbum, FeaturedAlbum, Song

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name', 'album_type']


admin.site.register(WeeksTop)
admin.site.register(NewHit)
admin.site.register(PopularAlbum)
admin.site.register(FeaturedAlbum)
admin.site.register(Song)