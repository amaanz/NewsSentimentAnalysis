# Generated by Django 5.0.6 on 2024-06-12 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsscore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='api_key',
            new_name='apikey',
        ),
    ]
