# Generated by Django 5.0.3 on 2024-04-05 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0012_genre"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="games",
            name="genre",
        ),
    ]