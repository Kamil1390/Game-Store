from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.db import models
from .models import Games, InfoBuy, Genre, Cover, GameInfo, MinSystemReq, RecSystemReq

cover = Cover.objects.get(pk=3)


def index(request: HttpRequest) -> HttpResponse:
    hits = Games.objects.order_by('-id')[:4].select_related("gameinfo")
    tournaments = Games.objects.filter(is_tournament=True).select_related("gameinfo")
    sale = Games.objects.filter(discount_percent__gte=15)[:4].select_related("gameinfo")
    data = {'hits': hits, 'tournaments': tournaments, 'sale': sale, 'cover': Cover.objects.filter(pk__lte=2)}
    return render(request, "main_app/index.html", context=data)


def catalog(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.select_related("gameinfo", "genre", "min_system_req", "recom_system_req").filter(price__gt=0).order_by("title")
    data = {'data_from_db': data_from_db, 'cover': cover, 'genre_selected': None}
    return render(request, "main_app/catalog.html", context=data)


def show_genre(request: HttpRequest, genre_slug: models.SlugField) -> HttpResponse:
    data_from_db = Games.objects.select_related("genre", "gameinfo").filter(price__gt=0, genre__slug=genre_slug).order_by("title")
    data = {'data_from_db': data_from_db, 'cover': cover, 'genre_selected': genre_slug}
    return render(request, "main_app/catalog.html", context=data)


def show_sale(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.select_related("genre", "gameinfo").filter(price__gt=0, discount_percent__gt=0).order_by("title")
    data = {'data_from_db': data_from_db, 'cover': cover, 'genre_selected': 0}
    return render(request, "main_app/catalog.html", context=data)


def info_buy(request: HttpRequest) -> HttpResponse:
    data_from_db = InfoBuy.objects.all()
    data = {'data_from_db': data_from_db, 'cover': Cover.objects.get(pk=4)}
    return render(request, "main_app/info_buy.html", context=data)


def show_game(request: HttpRequest, game_slug: models.SlugField) -> HttpResponse:
    gameinfo_db = get_object_or_404(GameInfo, game__slug=game_slug)
    games_db = get_object_or_404(Games, slug=game_slug)
    min_sys_db = get_object_or_404(MinSystemReq, game__slug=game_slug)
    rec_sys_db = get_object_or_404(RecSystemReq, game__slug=game_slug)
    main_info = {}
    data = {
        'gameinfo_db': gameinfo_db, 'games_db': games_db,
        'min_sys_db': min_sys_db, 'rec_sys_db': rec_sys_db
    }
    return render(request, "main_app/game.html", context=data)


def cart(request: HttpRequest, game) -> HttpResponse:
    data_from_db = get_object_or_404(Games, slug=genre_slug)
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/game.html", context=data)



