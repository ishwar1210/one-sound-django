from django.shortcuts import render, get_object_or_404
from .models import Event


# Create your views here.
def events(request):
    events = Event.objects.all().order_by('-event_date')  # Sort by newest events first
    return render(request, 'event.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})
