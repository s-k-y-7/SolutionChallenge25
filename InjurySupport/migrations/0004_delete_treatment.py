# Generated by Django 5.0.6 on 2025-03-29 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "InjurySupport",
            "0003_remove_injury_treatment_types_alter_treatment_name_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="Treatment",
        ),
    ]
