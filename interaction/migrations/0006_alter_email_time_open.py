# Generated by Django 4.1 on 2024-08-22 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0005_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='time_open',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
