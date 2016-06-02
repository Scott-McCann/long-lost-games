from django.shortcuts import render
from .models import Game, System, Company, Director, Publisher, Comment, Review, Review_Comment
from django.template import loader
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ContactForm, GameForm, ReviewForm, CommentForm
from .utils import get_next, get_previous

# Create your views here.
def index(request):
    return render(request, 'lostgames/index.html')

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

    all_things = Game.objects.all()
    next_id = get_next(all_things, game.id)
    previous_id = get_previous(all_things, game.id)

    context = { 'game': game,
                'next_id': next_id,
                'previous_id': previous_id}

    return render(request, 'lostgames/game_details.html', context)

#Game Forms Go Here.

@login_required
def create_game_form(request):
    if request.method == 'POST':
        form= GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return HttpResponseRedirect('/core/games/' + str(game.id))
    else:
        form = GameForm()

    return render(request, 'lostgames/create_game.html', { 'form':form })

@permission_required('lostgames.change_game')
def edit_game_form(request, game_id):

    try:
        game = Game.objects.get(id=game_id)
    except game.DoesNotExist:
        raise Http404("No such Game!")

    form = None
    if request.method == 'POST':
        form= GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            return HttpResponseRedirect('/core/games/' + str(game.id))

    else:
        form = GameForm(instance=game)


    context = { 'form': form,
                'game': game }

    return render(request, 'lostgames/edit_game.html', context)













#System views go here.
def view_systems(request):
    systems = System.objects.all()
    context = { 'systems': systems }

    return render(request, 'lostgames/systems.html', context)


def view_system_details(request, system_id):

    try:
        system = System.objects.get(id=system_id)
    except system.DoesNotExist:
        raise Http404("No System Found")

    all_things = System.objects.all()
    next_id = get_next(all_things, system.id)
    previous_id = get_previous(all_things, system.id)


    context = { 'system': system,
                'next_id': next_id,
                'previous_id': previous_id}


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

@permission_required('lostgames.add_comment')
def create_comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return HttpResponseRedirect('/core/comments/' + str(comment.id))
    else:
        form = CommentForm()

    return render(request, 'lostgames/create_comment.html', { 'form':form })



# @permission_required('lodthsmrd.moderate_comment')
# def moderate_comment(request, comment_id):
#     comment = Comment.objects.get(id=comment_id)
#      if request.method == 'POST':
#         form = CommentForm(request.POST)
#            if form.is_valid():
#      comment = form.save()
#      return HttpResponseRedirect('/core/comments/' + str(comment.id))
#     else:
#          pass
#          # show form












#Review Views


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


@permission_required('lostgames.change_review')
def edit_review_form(request, review_id):

    try:
        review = Review.objects.get(id=review_id)
    except review.DoesNotExist:
        raise Http404("No such Review!")

    form = None
    if request.method == 'POST':
        form= ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return HttpResponseRedirect('/core/reviews/' + str(review.id))

    else:
        form = ReviewForm(instance=review)


    context = { 'form': form,
                'review': review }

    return render(request, 'lostgames/edit_review.html', context)











#Review Comments

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


@permission_required('lostgames.add_review_comment')
def create_review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return HttpResponseRedirect('/core/reviews/' + str(review.id))
    else:
        form = ReviewForm()

    return render(request, 'lostgames/create_review.html', { 'form':form })



















#Form Views
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/core/games/')

    form = ContactForm()
    context = { 'form': form }

    return render(request, 'lostgames/contact.html', context)
