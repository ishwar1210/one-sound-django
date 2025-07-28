from django.shortcuts import render, get_object_or_404
from .models import Event


# Create your views here.
def events(request):
    events = Event.objects.all().order_by('-event_date')  # Sort by newest events first
    return render(request, 'event.html', {'events': events})

from datetime import date
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_upcoming = event.event_date >= date.today()

    event_price_paise = int(float(event.price) * 100)
    return render(request, 'events/event_detail.html', {
        'event': event,
        'event_price_paise': event_price_paise,
        'is_upcoming': is_upcoming
    })
