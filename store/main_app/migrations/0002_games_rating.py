# Generated by Django 5.0.3 on 2024-03-29 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="games",
            name="rating",
            field=models.FloatField(default=0.0),
        ),
    ]
