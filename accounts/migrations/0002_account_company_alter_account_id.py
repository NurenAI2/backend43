# Generated by Django 4.2.1 on 2024-03-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="company",
            field=models.CharField(default="Unknown", max_length=100),
        ),
        migrations.AlterField(
            model_name="account",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
