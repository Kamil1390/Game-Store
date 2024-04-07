from django.db import models


class Games(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    path_to_img = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(default=0.0)
    is_tournament = models.BooleanField(default=False)
    genre = models.ForeignKey(to='Genre', on_delete=models.PROTECT)
    discount_percent = models.FloatField(default=0.0)
    path_to_mini_img = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=15, default="action")
    analog_name = models.CharField(max_length=15, default="Шутеры")
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Info(models.Model):
    title = models.CharField(max_length=100)
    path_to_img = models.CharField(max_length=100)

    def __str__(self):
        return self.title
