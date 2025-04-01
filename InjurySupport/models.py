from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


# Injury Choices
INJURY_CHOICES = [
    ('strain', 'Strain'), ('tear', 'Tear'), ('cramp', 'Cramp'), ('sprain', 'Sprain'),
    ('dislocation', 'Dislocation'), ('fracture', 'Fracture'), ('stress_fracture', 'Stress Fracture'),
    ('tendonitis', 'Tendonitis'), ('ligament_tear', 'Ligament Tear'),
    ('concussion', 'Concussion'), ('whiplash', 'Whiplash'), ('shin_splint', 'Shin Splint'),
    ('tennis_elbow', 'Tennis Elbow'), ('pinched_nerve', 'Pinched Nerve'), ('sciatica', 'Sciatica'),
    ('abrasion', 'Abrasion'), ('blister', 'Blister'), ('other', 'Other')
]

# Severity Choices
SEVERITY_CHOICES = [('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')]

# Recovery Time Choices
RECOVERY_CHOICES = [
    ('less_than_week', 'Less than a week'),
    ('couple_weeks', 'Couple of weeks'),
    ('one_month', 'One Month'),
    ('couple_months', 'Couple of Months'),
    ('years', 'Years')
]

# Treatment Choices
TREATMENT_CHOICES = [
    ('physiotherapy', 'Physiotherapy'), ('surgery', 'Surgery'), ('medications', 'Medications'),
    ('rest', 'Rest and Immobilization'), ('rehab', 'Rehabilitation Exercises'),
    ('injection', 'Injection Therapy'), ('chiropractic', 'Chiropractic Care'),
    ('acupuncture', 'Acupuncture or Dry Needling'), ('cold_heat', 'Cold and Heat Therapy'),
    ('massage', 'Massage Therapy'), ('occupational', 'Occupational Therapy'),
    ('hydrotherapy', 'Hydrotherapy'), ('electrical', 'Electrical Stimulation Therapy')
]

TREATMENT_CHOICES_YES_NO = [
    ('yes', 'Yes'),
    ('no', 'No'),
]

# class Treatment(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True, choices=TREATMENT_CHOICES)

#     def __str__(self):
#         return self.name

class Injury(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    injury_type = models.CharField(max_length=50, choices=INJURY_CHOICES)
    other_injury = models.CharField(max_length=255, blank=True, null=True)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    recovery_time = models.CharField(max_length=20, choices=RECOVERY_CHOICES)
    treatment_taken = models.CharField(max_length=3, choices=TREATMENT_CHOICES_YES_NO, default='no')    
    medical_report = models.FileField(upload_to='medical_reports/', blank=True, null=True)
    # treatment_types = models.ManyToManyField(Treatment, blank=True)    
    treatment_types = MultiSelectField(choices=TREATMENT_CHOICES, blank=True, null=True)
    treatment_effectiveness = models.PositiveIntegerField(null=True, blank=True)
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.injury_type}"


# Body Parts
BODY_PART_CHOICES = [
    ('head', 'Head'), ('neck', 'Neck'), ('shoulder', 'Shoulder'), ('arm', 'Arm'), 
    ('elbow', 'Elbow'), ('wrist', 'Wrist'), ('hand', 'Hand'), ('chest', 'Chest'),
    ('back', 'Back'), ('stomach', 'Stomach'), ('hip', 'Hip'), ('leg', 'Leg'),
    ('knee', 'Knee'), ('ankle', 'Ankle'), ('foot', 'Foot'), ('other', 'Other')
]

# Pain Level
PAIN_LEVEL_CHOICES = [(i, str(i)) for i in range(1, 11)]

# Discomfort Type
DISCOMFORT_CHOICES = [
    ('ache', 'Ache'), ('sharp_pain', 'Sharp Pain'), ('throbbing', 'Throbbing'),
    ('burning', 'Burning'), ('stiffness', 'Stiffness'), ('numbness', 'Numbness'),
    ('tingling', 'Tingling'), ('other', 'Other')
]

# Possible Causes
CAUSE_CHOICES = [
    ('training', 'Training'), ('accident', 'Accident'), ('posture', 'Posture'),
    ('unknown', 'Unknown'), ('other', 'Other')
]

class SymptomLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body_part = models.CharField(max_length=20, choices=BODY_PART_CHOICES)
    pain_level = models.IntegerField(choices=PAIN_LEVEL_CHOICES)
    discomfort_type = models.CharField(max_length=20, choices=DISCOMFORT_CHOICES, blank=True, null=True)
    possible_cause = models.CharField(max_length=20, choices=CAUSE_CHOICES, blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    date_logged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.body_part} - Pain Level: {self.pain_level}"

class RestAndRecovery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sleep_hours = models.DecimalField(max_digits=4, decimal_places=2)
    sleep_quality = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    on_medication = models.BooleanField(default=False)
    medication_name = models.CharField(max_length=255, blank=True, null=True)
    medication_frequency = models.CharField(max_length=100, blank=True, null=True)
    recovery_progress = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    date_logged = models.DateField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('user', 'date_logged')

    def __str__(self):
        return f"{self.user.username} - {self.date_logged} - Sleep: {self.sleep_hours}h"
 


