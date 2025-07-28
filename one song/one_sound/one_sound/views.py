from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.decorators import login_required
from events.models import Event, Booking

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Make sure you have a 'login' url
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def uesr_login(request):
    print("Ishwar Login")
    return render(request,"login.html")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.user.email if request.user.is_authenticated else request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_message = f"From: {request.user.first_name} {request.user.last_name}\n\n Email: {request.user.email}\n\n Message: {message}"
        mail = EmailMessage(
            subject=subject or "Contact Request",
            body=full_message,
            from_email='onesound1210@gmail.com',
            to=['onesound1210@gmail.com'],
            reply_to=[email],
        )
        mail.send(fail_silently=False)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

@login_required
def profile(request):
    user = request.user
    bookings = Booking.objects.filter(user=user).order_by('-date')
    # Har booking ke liye amount calculate karo
    for booking in bookings:
        booking.amount = booking.event.price * booking.qty
    return render(request, 'profile.html', {
        'user': user,
        'bookings': bookings,
    })