# Generated by Django 4.2.1 on 2024-05-15 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("campaign", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="campaign_owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campaign_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
