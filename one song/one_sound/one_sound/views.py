from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from events.models import Event, Booking
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def uesr_login(request):
    return render(request, "login.html")

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
    message = None
    password_message = None

    if request.method == "POST":
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        message = "Profile updated successfully!"

        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if current_password and new_password and confirm_password:
            if user.check_password(current_password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    password_message = "Password changed successfully!"
                    update_session_auth_hash(request, user)
                else:
                    password_message = "New password and confirmation don't match!"
            else:
                password_message = "Current password is incorrect!"

    bookings = Booking.objects.filter(user=user).order_by('-date')
    for booking in bookings:
        booking.amount = booking.event.price * booking.qty

    return render(request, 'profile.html', {
        'user': user,
        'bookings': bookings,
        'message': message,
        'password_message': password_message,
    })