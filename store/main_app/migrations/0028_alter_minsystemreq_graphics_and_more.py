# Generated by Django 5.0.3 on 2024-04-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0027_remove_games_path_to_img_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="minsystemreq",
            name="graphics",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="minsystemreq",
            name="memory",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="minsystemreq",
            name="os",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="minsystemreq",
            name="processor",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="minsystemreq",
            name="storage",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="recsystemreq",
            name="graphics",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="recsystemreq",
            name="memory",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="recsystemreq",
            name="os",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="recsystemreq",
            name="processor",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="recsystemreq",
            name="storage",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]