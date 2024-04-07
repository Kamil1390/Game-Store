from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.db import models
from .models import Games, Info, Genre


def index(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.all()
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/index.html", context=data)


def catalog(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.filter(price__gt=0).order_by("title")
    for item in data_from_db:
        if item.discount_percent:
            item.discount_percent = item.price - int((item.discount_percent / 100 * item.price))
    genre_db = Genre.objects.all()
    data = {'data_from_db': data_from_db, 'genre_db': genre_db, 'genre_selected': 0}
    return render(request, "main_app/catalog.html", context=data)


def show_genre(request: HttpRequest, genre_slug: models.SlugField) -> HttpResponse:
    data_from_db = Games.objects.filter(price__gt=0, genre__slug=genre_slug).order_by("title")
    for item in data_from_db:
        if item.discount_percent:
            item.discount_percent = item.price - int((item.discount_percent / 100 * item.price))
    genre_db = Genre.objects.all()
    genre_selected = get_object_or_404(Genre, slug=genre_slug)
    data = {'data_from_db': data_from_db, 'genre_db': genre_db, 'genre_selected': genre_selected.pk}
    return render(request, "main_app/catalog.html", context=data)


def info(request: HttpRequest) -> HttpResponse:
    data_from_db = Info.objects.all()
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/info_buy.html", context=data)


def show_game(request: HttpRequest, game_slug: models.SlugField) -> HttpResponse:
    data_from_db = get_object_or_404(Games, slug=game_slug)
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/game.html", context=data)


# def show_genre(request: HttpRequest, genre_slug: models.SlugField) -> HttpResponse:
#     data_from_db = get_object_or_404(Games, slug=genre_slug)
#     data = {'data_from_db': data_from_db}
#     return render(request, "main_app/game.html", context=data)



