from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.db import models
from .models import Games, Info


def index(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.all()
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/index.html", context=data)


def catalog(request: HttpRequest) -> HttpResponse:
    data_from_db = Games.objects.filter(price__gt=0).order_by("title")
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/catalog.html", context=data)


def show_game(request: HttpRequest, game_slug: models.SlugField) -> HttpResponse:
    data_from_db = get_object_or_404(Games, slug=game_slug)
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/post.html", context=data)


def info(request: HttpRequest) -> HttpResponse:
    data_from_db = Info.objects.all()
    data = {'data_from_db': data_from_db}
    return render(request, "main_app/info_buy.html", context=data)
