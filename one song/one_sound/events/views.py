from django.shortcuts import render, get_object_or_404
from .models import Event, Booking
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Event
from django.contrib.auth.models import User
import qrcode
import base64
from io import BytesIO
from django.core.mail import EmailMultiAlternatives
from django.utils.html import format_html
from email.mime.image import MIMEImage
from datetime import date


# Create your views here.
def events(request):
    events = Event.objects.all().order_by('-event_date')  # Sort by newest events first
    return render(request, 'event.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_upcoming = event.event_date >= date.today()

    event_price_paise = int(float(event.price) * 100)
    return render(request, 'events/event_detail.html', {
        'event': event,
        'event_price_paise': event_price_paise,
        'is_upcoming': is_upcoming
    })


@csrf_exempt
@login_required
def send_booking_email(request):
    if request.method == "POST":
        event_id = request.POST.get('event_id')
        payment_id = request.POST.get('payment_id')
        qty = int(request.POST.get('qty', 1))
        event = Event.objects.get(pk=event_id)
        user = request.user

        # YAHAN BOOKING CREATE KARO
        Booking.objects.create(
            user=user,
            event=event,
            payment_id=payment_id,
            qty=qty
        )

        # Generate QR code
        qr_data = f"User: {user.first_name or user.username} {user.last_name}\n\n Event: {event.event_name}\n\n Date: {event.event_date}\n\n Venue: {event.venue}\n\n Qty: {qty}\n\n Payment ID: {payment_id}"
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)

        # Email content with embedded QR as attachment
        html_content = f"""
        <p>Dear {user.first_name or user.username},</p>
        <p>Your booking for <b>{event.event_name}</b> on <b>{event.event_date}</b> at <b>{event.venue}</b> is confirmed.</p>
        <p>Show this QR code at entry:</p>
        <img src="cid:qr_code_image" alt="QR Code" style="width:200px;height:200px;" />
        <p>Thank you!</p>
        """

        email = EmailMultiAlternatives(
            subject=f'Booking Confirmed for {event.event_name}',
            body="Your booking is confirmed. Please see the QR code in the email.",
            from_email=None,
            to=[user.email]
        )
        email.attach_alternative(html_content, "text/html")

        # Attach QR code image with Content-ID
        qr_image = MIMEImage(buffer.getvalue(), _subtype="png")
        qr_image.add_header('Content-ID', '<qr_code_image>')
        qr_image.add_header('Content-Disposition', 'inline', filename="qrcode.png")
        email.attach(qr_image)

        email.send()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)


def event_list(request):
    today = date.today()
    upcoming_events = Event.objects.filter(event_date__gte=today).order_by('event_date')
    passed_events = Event.objects.filter(event_date__lt=today).order_by('-event_date')
    return render(request, 'event.html', {
        'upcoming_events': upcoming_events,
        'passed_events': passed_events,
    })
