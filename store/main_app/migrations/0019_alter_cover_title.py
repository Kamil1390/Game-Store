# Generated by Django 5.0.3 on 2024-04-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0018_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cover",
            name="title",
            field=models.TextField(),
        ),
    ]
