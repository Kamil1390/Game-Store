from django.db import models
from django.urls import reverse
from django.utils import timezone


class Games(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    is_tournament = models.BooleanField(default=False)
    genre = models.ForeignKey(to='Genre', on_delete=models.PROTECT, related_name="cats")
    discount_percent = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)
    gameinfo = models.OneToOneField(to='GameInfo', on_delete=models.SET_NULL, blank=True, null=True, related_name="game")
    min_system_req = models.OneToOneField(to='MinSystemReq', on_delete=models.SET_NULL, blank=True, null=True, related_name="game")
    recom_system_req = models.OneToOneField(to='RecSystemReq', on_delete=models.SET_NULL, blank=True, null=True, related_name="game")

    def __str__(self):
        return self.title

    def discount_price(self):
        if self.discount_percent:
            discount = self.discount_percent / 100 * self.price
            return int(self.price - discount)

    def discount_points(self):
        return int(3 / 100 * self.price)

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


class InfoBuy(models.Model):
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


class GameInfo(models.Model):
    path_to_img = models.CharField(max_length=100, blank=True)
    path_to_mini_img = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(blank=True, max_length=100)
    developer = models.CharField(blank=True, max_length=100)
    date_release = models.DateField(default=timezone.now)
    local = models.CharField(blank=True, max_length=100)
    system = models.CharField(blank=True, max_length=100)
    age_rating = models.CharField(blank=True, max_length=3)
    description = models.TextField(blank=True)
    features = models.TextField(blank=True)

    def __str__(self):
        return f'{self.pk}'

    def list_features(self):
        return self.features.split('\n')

    def main_info(self):
        lst = [
            "Издатель", "Разработчик", "Дата выхода игры", "Жанр",
            "Локализация", "Система активации", "Возрастной рейтинг",
        ]
        lst_settings = [getattr(self, field.name) for field in self._meta.fields]
        lst_settings.insert(6, self.game.genre.analog_name)
        return zip(lst, lst_settings[3:])

    def list_description(self):
        lst = ["Описание игры", "Особенности игры"]
        lst_settings = [self.description, self.features.split('\n')]
        return zip(lst, lst_settings)


class MinSystemReq(models.Model):
    os = models.CharField(max_length=255, blank=True)
    processor = models.CharField(max_length=255, blank=True)
    memory = models.CharField(max_length=255, blank=True)
    graphics = models.CharField(max_length=255, blank=True)
    storage = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.os

    def list_min_system(self):
        lst = ["Операционная система", "Процессор", "Оперативная память", "Видеокарта", "Место на диске"]
        lst_settings = [getattr(self, field.name) for field in self._meta.fields]
        return zip(lst, lst_settings[1:])


class RecSystemReq(models.Model):
    os = models.CharField(max_length=255, blank=True)
    processor = models.CharField(max_length=255, blank=True)
    memory = models.CharField(max_length=255, blank=True)
    graphics = models.CharField(max_length=255, blank=True)
    storage = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.os

    def list_rec_system(self):
        lst = ["Операционная система", "Процессор", "Оперативная память", "Видеокарта", "Место на диске"]
        lst_settings = [getattr(self, field.name) for field in self._meta.fields]
        return zip(lst, lst_settings[1:])
