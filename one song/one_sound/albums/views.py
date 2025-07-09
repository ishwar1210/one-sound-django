from django.shortcuts import render
from .models import Album  # Make sure your model is actually named 'Album'

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