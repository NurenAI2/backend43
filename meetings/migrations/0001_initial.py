# Generated by Django 4.2.1 on 2024-05-15 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0003_account_tenant"),
    ]

    operations = [
        migrations.CreateModel(
            name="meetings",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="Title"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Location"
                    ),
                ),
                ("from_time", models.DateTimeField(verbose_name="From")),
                ("to_time", models.DateTimeField(verbose_name="To")),
                (
                    "related_to",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Related To"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "account",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="meetings",
                        to="accounts.account",
                    ),
                ),
            ],
        ),
    ]
