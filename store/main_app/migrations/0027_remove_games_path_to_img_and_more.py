# Generated by Django 5.0.3 on 2024-04-20 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0026_minsystemreq_recsystemreq_games_min_system_req_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="games",
            name="path_to_img",
        ),
        migrations.RemoveField(
            model_name="games",
            name="path_to_mini_img",
        ),
    ]
