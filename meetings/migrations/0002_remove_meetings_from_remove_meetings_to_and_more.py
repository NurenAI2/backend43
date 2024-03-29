# Generated by Django 4.2.1 on 2024-03-29 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contacts", "0002_alter_contact_id"),
        ("meetings", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meetings",
            name="from",
        ),
        migrations.RemoveField(
            model_name="meetings",
            name="to",
        ),
        migrations.AddField(
            model_name="meetings",
            name="from_time",
            field=models.DateTimeField(default='2024-01-01', verbose_name="From"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="meetings",
            name="to_time",
            field=models.DateTimeField(default='2024-01-01', verbose_name="To"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="meetings",
            name="contact_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meeting_contacts",
                to="contacts.contact",
                verbose_name="Contact Name",
            ),
        ),
        migrations.AlterField(
            model_name="meetings",
            name="host",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="meeting_hosts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Host",
            ),
        ),
        migrations.AlterField(
            model_name="meetings",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.RemoveField(
            model_name="meetings",
            name="participants",
        ),
        migrations.AddField(
            model_name="meetings",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="meeting_participants", to="contacts.contact"
            ),
        ),
    ]
