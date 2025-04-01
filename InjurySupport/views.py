from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, InjuryForm, SymptomLogForm, RestAndRecoveryForm
from .models import Injury
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'InjurySupport/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'InjurySupport/register.html', {'form': form})

@login_required(login_url='/injurysupport/login/')
def profile(request):
    return render(request, 'InjurySupport/profile.html')

@login_required(login_url='/injurysupport/login/')
def injury_list(request):
    injuries = Injury.objects.filter(user=request.user)
    return render(request, 'InjurySupport/injury_list.html', {'injuries': injuries})

@login_required(login_url='/injurysupport/login/')
def add_injury(request):
    if request.method == 'POST':
        form = InjuryForm(request.POST, request.FILES)
        if form.is_valid():
            injury = form.save(commit=False)
            injury.user = request.user
            injury.save()
            return redirect('injury_list')
    else:
        form = InjuryForm()
    return render(request, 'InjurySupport/add_injury.html', {'form': form})

@login_required(login_url='/injurysupport/login/')
def log_symptom(request):
    if request.method == 'POST':
        form = SymptomLogForm(request.POST)
        if form.is_valid():
            symptom = form.save(commit=False)
            symptom.user = request.user
            symptom.save()
            return redirect('suggestion')
    else:
        form = SymptomLogForm()
    return render(request, 'InjurySupport/log_symptom.html', {'form': form})

@login_required(login_url='/injurysupport/login/')
def suggestion(request):
    return render(request, 'InjurySupport/suggestion.html')

@login_required(login_url='/injurysupport/login/')
def rest_and_recovery(request):
    if request.method == 'POST':
        form = RestAndRecoveryForm(request.POST)
        if form.is_valid():
            recovery_data = form.save(commit=False)
            recovery_data.user = request.user
            recovery_data.save()
            return redirect('rest_suggestions')
    else:
        form = RestAndRecoveryForm()
    return render(request, 'InjurySupport/rest_and_recovery.html', {'form': form})

@login_required(login_url='/injurysupport/login/')
def rest_suggestions(request):
    return render(request, 'InjurySupport/rest_suggestions.html')

def test_view(request):
    return HttpResponse("Template path is correct.")
