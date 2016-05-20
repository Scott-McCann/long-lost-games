from django.shortcuts import render
from .models import Game, System, Company, Director, Publisher, Comment, Review, Review_Comment 
from django.template import loader
from django.http import HttpResponse, Http404
# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome to the Core</h1>')

#Game views go here.
def view_games(request):
    games = Game.objects.all()
    templ = loader.get_template('lostgames/games.html')

    context = {'games': games}

    return HttpResponse(templ.render(context, request))

def view_game_details(request, game_id):

    try:
        game = Game.objects.get(id=game_id)
    except game.DoesNotExist:
        raise Http404("No such Game!")

    context = { 'game': game }

    return render(request, 'lostgames/game_details.html', context)

#System views go here.
def view_systems(request):
    systems = System.objects.all()
    context = {'systems': systems }

    return render(request, 'lostgames/systems.html', context)

def view_system_details(request, system_id):

    try:
        system = System.objects.get(id=system_id)
    except system.DoesNotExist:
        raise Http404("No System Found")

    context = { 'system': system }

    return render(request, 'lostgames/system_details.html', context)

#Company views go here.
def view_companies(request):
    companies = Company.objects.all()
    context = { 'companies': companies }

    return render(request, 'lostgames/companies.html', context)

def view_company_details(request, company_id):

    try:
        company = Company.objects.get(id=company_id)
    except company.DoesNotExist:
        raise Http404("No Such Company")

    context = { 'company': company }

    return render(request, 'lostgames/company_details.html', context)

#Director views go here
def view_directors(request):
    directors = Director.objects.all()
    context = { 'directors': directors }

    return render(request, 'lostgames/directors.html', context)

def view_director_details(request, director_id):

    try:
        director = Director.objects.get(id=director_id)
    except director.DoesNotExist:
        raise Http404("That director has not been born yet.")

    context = { 'director': director }

    return render(request, 'lostgames/director_details.html', context)

#Publihser views go here.
def view_publishers(request):
    publishers = Publisher.objects.all()
    context = { 'publishers': publishers }

    return render(request, 'lostgames/publishers.html', context)

def view_publisher_details(request, publisher_id):

    try:
        publisher = Publisher.objects.get(id=publisher_id)
    except publisher.DoesNotExist:
        raise Http404("Publisher not published here.")

    context = { 'publisher': publisher }

    return render(request, 'lostgames/publisher_details.html', context)

#Commnet views go here.
def view_comments(request):
    comments = Comment.objects.all()
    context = { 'comments': comments }

    return render(request, 'lostgames/comments.html', context)

def view_comment_details(request, comment_id):

    try:
        comment = Comment.objects.get(id=comment_id)
    except comment.DoesNotExist:
        raise Http404("This comment is either missing or non-existant")

    context = { 'comment': comment }

    return render(request, 'lostgames/comment_details.html', context)

def view_reviews(request):
    reviews = Review.objects.all()
    context = { 'reviews': reviews }

    return render(request, 'lostgames/reviews.html', context)

def view_review_details(request, review_id):

    try:
        review = Review.objects.get(id=review_id)
    except review.DoesNotExist:
        raise Http404("This review is either missing or non-existant")

    context = { 'review': review }

    return render(request, 'lostgames/review_details.html', context)


def view_review_comments(request):
    review_comments = Review_Comment.objects.all()
    context = { 'review_comments': review_comments }

    return render(request, 'lostgames/review_comments.html', context)

def view_review_comment_details(request, review_comment_id):

    try:
        review_comment = Review_Comment.objects.get(id=review_comment_id)
    except review_comment.DoesNotExist:
        raise Http404("This comment is either missing or non-existant")

    context = { 'review_comment': review_comment }

    return render(request, 'lostgames/review_comment_details.html', context)
