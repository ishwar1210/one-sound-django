from django.shortcuts import render
from albums.models import Album, FeaturedAlbum, WeeksTop, NewHit, PopularAlbum
from events.models import Event
from news.models import News

def index(request):
    albums = Album.objects.all()[:6]
    top_albums = [wt.album for wt in WeeksTop.objects.order_by('position')]
    new_hits = [nh.album for nh in NewHit.objects.order_by('position')]
    popular_albums = [pa.album for pa in PopularAlbum.objects.order_by('position')]
    featured_albums = FeaturedAlbum.objects.all()[:2]
    latest_event = Event.objects.order_by('-event_date').first()
    latest_news = News.objects.order_by('-published_date').first()  # ya jo bhi date field hai

    context = {
        'albums': albums,
        'top_albums': top_albums,
        'new_hits': new_hits,
        'popular_albums': popular_albums,
        'featured_albums': featured_albums,
        'latest_event': latest_event,
        'latest_news': latest_news,
    }
    return render(request, 'index.html', context)



