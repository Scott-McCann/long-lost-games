from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from datetime import date
from lostgames.models import Game
from . import views

class GamesTestCase(TestCase):
    def setUp(self):
        Game.objects.create(title="Test #1", release_date=date.today(), is_shown=True)
        Game.objects.create(title="Test #2", release_date=date.today(), is_shown=False)
        Game.objects.create(title="Test #3", release_date=date.today(), is_shown=True)

    def testGameFields(self):
        first = Game.objects.get(title="Test #1")
        self.assertEquals("Test #1", first.title)

    def testGetGames(self):
        games = Game.objects.all()
        self.assertEquals(3, len(games))

    def testGameIndex(self):
        client = Client()
        resp = client.get(reverse('game:games-index'))
        self.assertEquals(200, resp.status_code)
        self.assertContains(resp, "Showing")

    def testGameView(self):
        client = Client()
        game = Game.objects.order_by("id")[0]
        url = '/core/games/'+ str(game.id) + '/'
        resp = client.get(url)
        self.assertContains(resp, game.title)
        
# Create your tests here.
