from django import template
import main_app.views as views
from main_app.models import Genre, GameInfo

register = template.Library()


@register.inclusion_tag('main_app/list_main_cover.html')
def show_main_cover(data_from_db):
    return {'cover': data_from_db}


@register.inclusion_tag('main_app/list_categories.html')
def show_category(genre_selected):
    genre_db = Genre.objects.all()
    return {'genre_selected': genre_selected, 'genre_db': genre_db}


@register.inclusion_tag('main_app/list_games.html')
def show_games(data_from_db):
    return {'data_from_db': data_from_db}


@register.inclusion_tag('main_app/cover_page.html')
def show_cover(data):
    return {'data': data}


@register.inclusion_tag('main_app/list_info.html')
def show_info(data_from_db):
    return {'data_from_db': data_from_db}


@register.inclusion_tag('main_app/list_news.html')
def show_news(data_from_db):
    return {'data_from_db': data_from_db}


@register.inclusion_tag('main_app/list_tournaments.html')
def show_tournaments(data_from_db):
    return {'data_from_db': data_from_db}


@register.inclusion_tag('main_app/list_sales.html')
def show_sales(data_from_db):
    return {'sale': data_from_db}


@register.inclusion_tag('main_app/list_description.html')
def show_description(data_from_db):
    return {'data_from_db': data_from_db}
