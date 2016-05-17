from . import views
from django.conf.urls import url
from .models import Game
urlpatterns = [
    url(r'^$', views.index, name='games-index'),
    url(r'^(?P<game_id>[0-9]+)/$', views.view_game, name='content-view_game')

]
