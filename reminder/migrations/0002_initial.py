# Generated by Django 4.2.1 on 2024-05-15 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("reminder", "0001_initial"),
        ("tenant", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reminder",
            name="createdBy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reminder_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="reminder",
            name="tenant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tenant.tenant"
            ),
        ),
    ]
