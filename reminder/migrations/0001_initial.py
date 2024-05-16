# Generated by Django 4.2.1 on 2024-05-15 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reminder",
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
                ("subject", models.CharField(max_length=255)),
                (
                    "trigger_type",
                    models.CharField(
                        choices=[("event", "Event Trigger"), ("time", "Time Trigger")],
                        max_length=10,
                    ),
                ),
                ("event_date_time", models.DateTimeField(blank=True, null=True)),
                ("time_trigger", models.DateTimeField(blank=True, null=True)),
                ("is_triggered", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
