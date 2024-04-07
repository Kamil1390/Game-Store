from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("catalog/<slug:genre_slug>/", views.show_genre, name="genre"),
    path("info/", views.info, name="info"),
    path("<slug:game_slug>/", views.show_game, name="game"),
    ]
