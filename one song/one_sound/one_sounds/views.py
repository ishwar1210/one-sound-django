from django.shortcuts import render
from albums.models import Album  # Import from albums app

# Create your views here.


def index(request):
    albums = Album.objects.all()[:10]  # Latest 10 albums
    top_albums = Album.objects.all()[:6]  # Top 6 albums
    new_hits = Album.objects.all().order_by('-id')[:6]  # 6 newest albums
    popular_albums = Album.objects.all()[:7]  # 7 popular albums
    
    context = {
        'albums': albums,
        'top_albums': top_albums,
        'new_hits': new_hits,
        'popular_albums': popular_albums,
    }
    return render(request, 'index.html', context)

def register(request):
    return render(request, 'register.html')

