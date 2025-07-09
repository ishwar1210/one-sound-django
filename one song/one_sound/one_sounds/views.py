from django.shortcuts import render
from albums.models import Album
# Create your views here.

def index(request):
    context = {"albums": Album.objects.all()}
    return render(request, 'index.html', context)

