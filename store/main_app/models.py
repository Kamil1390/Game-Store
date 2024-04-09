from django.db import models
from django.urls import reverse


class Games(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    path_to_img = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(default=0.0)
    is_tournament = models.BooleanField(default=False)
    genre = models.ForeignKey(to='Genre', on_delete=models.PROTECT, related_name="cats")
    discount_percent = models.FloatField(default=0.0)
    path_to_mini_img = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)

    def __str__(self):
        return self.title

    def discount_price(self):
        if self.discount_percent:
            discount = self.discount_percent / 100 * self.price
            return int(self.price - discount)

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.slug})


class Genre(models.Model):
    name = models.CharField(max_length=15, default="action")
    analog_name = models.CharField(max_length=15, default="Шутеры")
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_slug': self.slug})


class Info(models.Model):
    title = models.CharField(max_length=100)
    path_to_img = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Cover(models.Model):
    title = models.TextField()
    description = models.TextField()
    path_to_img = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def title_list(self):
        return self.title.split()
