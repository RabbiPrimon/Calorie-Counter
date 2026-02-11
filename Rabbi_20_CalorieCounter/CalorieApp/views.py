from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from .forms import UserRegisterForm, UserProfileForm, DailyConsumptionForm
from .models import UserProfile, DailyConsumption
from django.utils import timezone
from datetime import date

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

@login_required
def dashboard(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    bmr = 0
    if profile:
        if profile.gender == 'M':
            bmr = 66.47 + (13.75 * profile.weight) + (5.003 * profile.height) - (6.755 * profile.age)
        else:
            bmr = 655.1 + (9.563 * profile.weight) + (1.850 * profile.height) - (4.676 * profile.age)
    
    today = date.today()
    consumed_today = DailyConsumption.objects.filter(user=request.user, date=today).aggregate(total=models.Sum('calories'))['total'] or 0
    
    consumptions = DailyConsumption.objects.filter(user=request.user, date=today)
    
    context = {
        'bmr': round(bmr, 2),
        'consumed_today': consumed_today,
        'consumptions': consumptions,
    }
    return render(request, 'dashboard.html', context)

@login_required
def add_consumption(request):
    if request.method == 'POST':
        form = DailyConsumptionForm(request.POST)
        if form.is_valid():
            consumption = form.save(commit=False)
            consumption.user = request.user
            consumption.date = timezone.now().date()
            consumption.save()
            messages.success(request, 'Consumption added!')
            return redirect('dashboard')
    else:
        form = DailyConsumptionForm()
    return render(request, 'add_consumption.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
