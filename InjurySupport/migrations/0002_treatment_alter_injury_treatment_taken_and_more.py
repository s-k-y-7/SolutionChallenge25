# Generated by Django 5.0.6 on 2025-03-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("InjurySupport", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Treatment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="injury",
            name="treatment_taken",
            field=models.CharField(
                choices=[("yes", "Yes"), ("no", "No")], default="no", max_length=3
            ),
        ),
        migrations.RemoveField(
            model_name="injury",
            name="treatment_types",
        ),
        migrations.AddField(
            model_name="injury",
            name="treatment_types",
            field=models.ManyToManyField(blank=True, to="InjurySupport.treatment"),
        ),
    ]
