from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.db import models
from .models import Games, InfoBuy, Genre, Cover, GameInfo

cover = Cover.objects.get(pk=3)


def index(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.all()
    sale = Games.objects.filter(discount_percent__gte=15)[:4]
    data = {'data_from_db': data_from_db, 'sale': sale, 'cover': Cover.objects.filter(pk__lte=2)}
    return render(request, "main_app/index.html", context=data)


def catalog(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.filter(price__gt=0).order_by("title")
    data = {'data_from_db': data_from_db, 'cover': cover, 'genre_selected': None}
    return render(request, "main_app/catalog.html", context=data)


def show_genre(request: HttpRequest, genre_slug: models.SlugField) -> HttpResponse:
    data_from_db = Games.objects.filter(price__gt=0, genre__slug=genre_slug).order_by("title")
    data = {'data_from_db': data_from_db, 'cover': cover, 'genre_selected': genre_slug}
    return render(request, "main_app/catalog.html", context=data)


def show_sale(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.filter(price__gt=0, discount_percent__gt=0).order_by("title")
    data = {'data_from_db': data_from_db, 'cover': cover, 'genre_selected': 0}
    return render(request, "main_app/catalog.html", context=data)


def info_buy(request: HttpRequest) -> HttpResponse:
    data_from_db = InfoBuy.objects.all()
    data = {'data_from_db': data_from_db, 'cover': Cover.objects.get(pk=4)}
    return render(request, "main_app/info_buy.html", context=data)


def show_game(request: HttpRequest, game_slug: models.SlugField) -> HttpResponse:
    lst = [
        "Издатель", "Разработчик", "Дата выхода игры",
        "Локализация", "Система активации", "Возрастной рейтинг",
    ]
    data_from_db = get_object_or_404(GameInfo, game__slug=game_slug)
    # data_game = GameInfo.game.get
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/game.html", context=data)


# def show_genre(request: HttpRequest, genre_slug: models.SlugField) -> HttpResponse:
#     data_from_db = get_object_or_404(Games, slug=genre_slug)
#     data = {'data_from_db': data_from_db}
#     return render(request, "main_app/game.html", context=data)



