from django.shortcuts import render
from .models import Game
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index(request):
    games = Game.objects.all()
    templ = loader.get_template('lostgames/games.html')

    context = {'games': games}

    return HttpResponse(templ.render(context, request))
