# Generated by Django 5.0.3 on 2024-04-05 23:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0013_remove_games_genre"),
    ]

    operations = [
        migrations.AddField(
            model_name="games",
            name="genre",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="main_app.genre",
            ),
        ),
    ]
