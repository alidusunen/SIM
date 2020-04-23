from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logofficer', 'logassistant'])
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request, 'Username OR Password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')