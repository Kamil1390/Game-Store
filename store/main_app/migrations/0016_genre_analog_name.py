# Generated by Django 5.0.3 on 2024-04-07 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0015_alter_games_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="genre",
            name="analog_name",
            field=models.CharField(default="Шутеры", max_length=15),
        ),
    ]
