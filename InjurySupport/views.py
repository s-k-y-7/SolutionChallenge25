from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, InjuryForm, SymptomLogForm, RestAndRecoveryForm
from .models import Injury, SymptomLog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
import os


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
def delete_injury(request, injury_id):
    injury = get_object_or_404(Injury, id=injury_id, user=request.user)
    injury.delete()
    return redirect('injury_list')



@login_required(login_url='/injurysupport/login/')
def log_symptom(request):
    if request.method == 'POST':
        form = SymptomLogForm(request.POST)
        if form.is_valid():
            symptom = form.save(commit=False)
            symptom.user = request.user
            symptom.save()

            # Prepare input for AI
            user_input = f"User has reported symptoms: {symptom.discomfort_type} in {symptom.body_part} with a pain level of {symptom.pain_level}. Possible cause: {symptom.possible_cause}. Additional symptoms: {symptom.other_details}."

            # Get AI-generated suggestion
            suggestion = get_ai_suggestion(user_input)

            # Store AI response in session
            request.session['ai_suggestion'] = suggestion

            return redirect('suggestion')  # Redirect to suggestion page
    else:
        form = SymptomLogForm()
    
    return render(request, 'InjurySupport/log_symptom.html', {'form': form})


@login_required(login_url='/injurysupport/login/')
def suggestion(request):
    return render(request, 'InjurySupport/suggestion.html')


@login_required(login_url='/injurysupport/login/')
def rest_and_recovery(request):
    latest_injury = Injury.objects.filter(user=request.user).order_by('-date_logged').first()
    #latest_symptom = SymptomLog.objects.filter(user=request.user).order_by('-date_logged').first()

    # Extract the relevant "recovering from" data
    recovering_from = f"{latest_injury.injury_type.replace('_', ' ').title() if latest_injury and latest_injury.injury_type else ''}"


    # if latest_symptom:
    #     recovering_from = f"{latest_symptom.body_part} - {latest_symptom.discomfort_type}"  # Example: "Knee - Sharp pain"
    # elif latest_injury:
    #     recovering_from = f"{latest_injury.injury_type}"  # Example: "Shoulder - Dislocation"

    if request.method == 'POST':
        form = RestAndRecoveryForm(request.POST)
        if form.is_valid():
            recovery_data = form.save(commit=False)
            recovery_data.user = request.user
            user_input_recovering_from = request.POST.get('recovering_from', recovering_from)  #Gets user input

            recovery_data.recovering_from = user_input_recovering_from  #Uses the edited value
            recovery_data.save()
            

            # Prepare input for AI
            user_input = (
                f"User is recovering from {recovery_data.recovering_from}. "
                f"Slept for {recovery_data.sleep_hours} hours with a quality rating of {recovery_data.sleep_quality}/10. "
                f"Medications taken: {recovery_data.on_medication}. "
                f"Perceived recovery progress: {recovery_data.recovery_progress}/10."
            )

            # Get AI-generated suggestion
            suggestion = get_ai_suggestion(user_input)

            # Store AI response in session
            request.session['ai_suggestion'] = suggestion

            return redirect('rest_suggestions')  # Redirect to rest_suggestions page
    else:
        form = RestAndRecoveryForm(initial={'recovering_from': recovering_from})

    return render(request, 'InjurySupport/rest_and_recovery.html', {'form': form, 'recovering_from': recovering_from})



@login_required(login_url='/injurysupport/login/')
def rest_suggestions(request):
    return render(request, 'InjurySupport/rest_suggestions.html')



# Set up Gemini API key (replace with your actual key)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_ai_suggestion(user_input):
    """
    Sends data to Gemini API and returns the AI-generated suggestion.
    """
    model = genai.GenerativeModel("gemini-2.5-pro-exp-03-25")
    # Modify the input to include the new system instruction
    response = model.generate_content(
        f""" 
        Based on the following health details, provide a **short, clear, and actionable** response. 
        No repetition of input. No unnecessary details. 
        Only **direct, practical advice** in 5-6 lines. 
        Symptoms: {user_input}
        """
    )
    
    
    return response.text if response and response.text else "No response from AI."


def test_view(request):
    return HttpResponse("Template path is correct.")
