from django import forms
from .models import Injury,  TREATMENT_CHOICES, SymptomLog, RestAndRecovery
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class InjuryForm(forms.ModelForm):
    class Meta:
        model = Injury
        fields = ['injury_type', 'other_injury', 'severity', 'recovery_time', 'treatment_taken', 'treatment_types', 'medical_report', 'treatment_effectiveness']
        widgets = {
            'injury_type': forms.Select(attrs={'class': 'form-control'}),
            'severity': forms.Select(attrs={'class': 'form-control'}),
            'recovery_time': forms.Select(attrs={'class': 'form-control'}),
            'treatment_taken': forms.RadioSelect(),
            'treatment_types': forms.CheckboxSelectMultiple(choices=TREATMENT_CHOICES),
            'treatment_effectiveness': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
        }


class SymptomLogForm(forms.ModelForm):
    class Meta:
        model = SymptomLog
        fields = ['body_part', 'pain_level', 'discomfort_type', 'possible_cause', 'other_details']
        widgets = {
            'body_part': forms.Select(attrs={'class': 'form-control'}),
            'pain_level': forms.Select(attrs={'class': 'form-control'}),
            'discomfort_type': forms.Select(attrs={'class': 'form-control'}),
            'possible_cause': forms.Select(attrs={'class': 'form-control'}),
            'other_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class RestAndRecoveryForm(forms.ModelForm):
    class Meta:
        model = RestAndRecovery
        fields = ['sleep_hours', 'sleep_quality', 'on_medication', 'medication_name', 'medication_frequency', 'recovery_progress']
        widgets = {
            'sleep_hours': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'sleep_quality': forms.Select(choices=[(i, str(i)) for i in range(1, 11)], attrs={'class': 'form-control'}),
            'on_medication': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'medication_name': forms.TextInput(attrs={'class': 'form-control'}),
            'medication_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'recovery_progress': forms.Select(choices=[(i, str(i)) for i in range(1, 11)], attrs={'class': 'form-control'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




