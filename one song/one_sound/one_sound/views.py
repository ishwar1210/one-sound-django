from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

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
    return render(request,"login.html")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")