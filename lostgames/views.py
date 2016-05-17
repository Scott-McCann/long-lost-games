from django.shortcuts import render
from .models import Game
from django.template import loader
from django.http import HttpResponse, Http404
# Create your views here.
def index(request):
    games = Game.objects.all()
    templ = loader.get_template('lostgames/games.html')

    context = {'games': games}

    return HttpResponse(templ.render(context, request))

def view_game(request, game_id):

    try:
        game = Game.objects.get(id=game_id)
    except game.DoesNotExist:
        raise Http404("No such Game!")
    context = { 'game': game }

    return render(request, 'lostgames/game_details.html', context)
