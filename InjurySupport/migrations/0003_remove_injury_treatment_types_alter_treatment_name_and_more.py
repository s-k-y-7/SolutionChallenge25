# Generated by Django 5.0.6 on 2025-03-29 07:32

import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("InjurySupport", "0002_treatment_alter_injury_treatment_taken_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="injury",
            name="treatment_types",
        ),
        migrations.AlterField(
            model_name="treatment",
            name="name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("physiotherapy", "Physiotherapy"),
                    ("surgery", "Surgery"),
                    ("medications", "Medications"),
                    ("rest", "Rest and Immobilization"),
                    ("rehab", "Rehabilitation Exercises"),
                    ("injection", "Injection Therapy"),
                    ("chiropractic", "Chiropractic Care"),
                    ("acupuncture", "Acupuncture or Dry Needling"),
                    ("cold_heat", "Cold and Heat Therapy"),
                    ("massage", "Massage Therapy"),
                    ("occupational", "Occupational Therapy"),
                    ("hydrotherapy", "Hydrotherapy"),
                    ("electrical", "Electrical Stimulation Therapy"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="injury",
            name="treatment_types",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[
                    ("physiotherapy", "Physiotherapy"),
                    ("surgery", "Surgery"),
                    ("medications", "Medications"),
                    ("rest", "Rest and Immobilization"),
                    ("rehab", "Rehabilitation Exercises"),
                    ("injection", "Injection Therapy"),
                    ("chiropractic", "Chiropractic Care"),
                    ("acupuncture", "Acupuncture or Dry Needling"),
                    ("cold_heat", "Cold and Heat Therapy"),
                    ("massage", "Massage Therapy"),
                    ("occupational", "Occupational Therapy"),
                    ("hydrotherapy", "Hydrotherapy"),
                    ("electrical", "Electrical Stimulation Therapy"),
                ],
                max_length=134,
                null=True,
            ),
        ),
    ]
