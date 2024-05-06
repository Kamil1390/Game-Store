from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("catalog/", views.catalog, name="catalog"),
    path("catalog/sale/", views.show_sale, name="sale"),
    path("catalog/<slug:genre_slug>/", views.show_genre, name="genre"),
    path("info/", views.info_buy, name="info"),
    path("<slug:game_slug>/", views.show_game, name="game"),
    path("cart/", views.cart, name="cart"),
    ]
