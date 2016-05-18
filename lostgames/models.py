from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=256)
    release_date = models.DateField()
    systems = models.ManyToManyField('System', null=False)
    company = models.ForeignKey('Company', null=True)
    publisher = models.ForeignKey('Publisher', null=True, on_delete=models.SET_NULL)
    director = models.ForeignKey('Director', null=True, on_delete=models.SET_NULL)
    plot_summary = models.TextField()
    views = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return self.title

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


class Comments(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=False, max_length=2500)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_text = models.TextField(blank=False)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0, null=False)

class Review_Comment(models.Model):
    review = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment_text = models.TextField(blank=False, max_length=2500)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0, null=False)
