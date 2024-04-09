from django import template
import main_app.views as views
from main_app.models import Genre

register = template.Library()


@register.inclusion_tag('main_app/list_categories.html')
def show_category(genre_selected):
    genre_db = Genre.objects.all()
    return {'genre_selected': genre_selected, 'genre_db': genre_db}


@register.inclusion_tag('main_app/list_games.html')
def show_games(data_from_db):
    return {'data_from_db': data_from_db}
