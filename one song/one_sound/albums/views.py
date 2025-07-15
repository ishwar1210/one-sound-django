from django.shortcuts import render ,get_object_or_404
from albums.models import Album, Song # Make sure your model is actually named 'Album'

# Create your views here.
def albums_list(request):
    context = {"albums": Album.objects.all()}
    return render(request, "albums.html", context)

def album_list(request):
    letter = request.GET.get('letter')
    
    if letter:
        if letter == '0-9':
            albums = Album.objects.filter(album_name__regex=r'^[0-9]')
        else:
            albums = Album.objects.filter(album_name__istartswith=letter)
    else:
        albums = Album.objects.all()

    return render(request, 'albums.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    songs = Song.objects.filter(album=album)  
    context = {
        'album': album,
        'songs': songs,  
    }
    return render(request, 'albums/album_detail.html', context)