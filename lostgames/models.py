
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from dateutil.relativedelta import relativedelta
from .utils import title_Case

class GenreGameQuerySet(models.QuerySet):
    def adventure(self):
        return self.filter(category='ADVENTURE')

    def action(self):
        return self.fitler(category='ACTION')

class ShownGameManager(models.Manager):
    def get_queryset(self):
        return super(ShownGameManager, self).get_queryset().filter(is_shown=True)

class HiddenGameManager(models.Manager):
    def get_queryset(self):
        return super(HiddenGameManager, self).get_queryset().filter(is_shown=False)




class Game(models.Model):
    Genre = (
    ('ACTION', 'Action'),
    ('ADVENTURE', 'Adventure'),
    ('STEALTH', 'Stealth'),
    ('FPS', 'First-Person Shooter'),
    ('PUZZLE', 'Puzzle'),
    ('SIM','Simulator'),
    ('OPEN_WORLD','Open World'),
    ('RPG','Role-Playing Game'),
    ('JRPG', 'Japanese Role-Playing Game'),
    ('STRATEGY', 'Strategy'),
    ('MMO', 'Massively Mutliplayer OnLine'),
    ('PLATFORM', 'Platform'),
    ('MOBA', 'Mutliplayer Online Battle Arena'),
    ('INDIE', 'Indie')
    )
    category = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        choices=Genre,
        default="Adventure")

    title = models.CharField(max_length=256)

    release_date = models.DateField(db_index=True)
    systems = models.ManyToManyField('System')
    company = models.ForeignKey('Company', null=True)
    publisher = models.ForeignKey('Publisher', null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey('Director', null=True, on_delete=models.SET_NULL)
    plot_summary = models.TextField()
    views = models.PositiveIntegerField(default=0, null=False, db_index=True)
    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    is_shown =  models.BooleanField(null=False, default=False, db_index=True)

    def better_Title(self):

        return title_Case(self.title)


    @property
    def age(self):

        return relativedelta(date.today(), self.release_date)

    def __str__(self):
        return self.title



    class Meta:
        permissions = (
            ("view_unshown_Game", "Can see games that have not been shown."),
        )








class System(models.Model):
    name = models.CharField(max_length=256)
    company = models.ForeignKey('Company', null=True, on_delete=models.SET_NULL)
    release_date = models.DateField()

    def __str__(self):
        return self.name






class Company(models.Model):
    name = models.CharField(max_length=256)
    date_founded = models.DateField()
    ceo = models.CharField(max_length=256)

    def __str__(self):
        return self.name






class Director(models.Model):
    name = models.CharField(max_length=256)
    bio = models.TextField()


    def __str__(self):
        return self.name





class Publisher(models.Model):
    name = models.CharField(max_length=256)
    date_founded = models.DateField()
    ceo = models.CharField(max_length=256)

    def __str__(self):
        return self.name





class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=False, max_length=2500)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    moderated = models.BooleanField(default=False, null=False)

    def __str__(self):
        return str(self.id) + ' ' + str(self.game) + '   -by: ' + str(self.user)

    def game_Case(self):
        return title_Case(self.game)

    def age(self):
        return relativedelta(date.today(), self.created)

    class Meta:
        permissions = (
            ("view_unmoderated_comment", "Can view unmoderated comments"),
            ("moderate_comment", "Can moderate comments"),
        )






class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_text = models.TextField(blank=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return str(self.id) + ' : ' + str(self.game) + '   -Submitted by: ' + str(self.user)

    def age(self):
        return relativedelta(date.today(), self.created)

    def game_Case(self):
        return title_Case(self.game)





class Review_Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=False, max_length=2500)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0, null=False)


    def __str__(self):
        return '#'+str(self.id) + '-- ' + str(self.review) +'--' + '   -by: ' + str(self.user)

    def age(self):
        return relativedelta(date.today(), self.created)

    def game_Case(self):
        return title_Case(self.review)
