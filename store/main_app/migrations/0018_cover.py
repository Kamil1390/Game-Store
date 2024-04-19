# Generated by Django 5.0.3 on 2024-04-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0017_alter_games_genre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cover",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("path_to_img", models.CharField(max_length=100)),
            ],
        ),
    ]