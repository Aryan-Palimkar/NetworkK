# Generated by Django 5.1.4 on 2025-01-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_remove_startup_contact_opening_startup_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='contact',
            field=models.URLField(blank=True, null=True),
        ),
    ]
