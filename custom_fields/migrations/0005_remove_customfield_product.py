# Generated by Django 4.1 on 2024-08-13 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_fields', '0004_customfield_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customfield',
            name='product',
        ),
    ]
