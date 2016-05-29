from . import views
from django.conf.urls import url
from .models import Game, System, Company, Director, Publisher, Comment

app_name = 'game'

urlpatterns = [

    url(r'^$', views.index, name='core-index'),
    #Game URLs go Here.
    url(r'^games/$', views.view_games, name='games-index'),
    url(r'^games/(?P<game_id>[0-9]+)/$', views.view_game_details, name='game_details'),
    url(r'^games/create/$', views.create_game_form, name='create_game'),
    url(r'^games/(?P<game_id>[0-9]+)/edit/$', views.edit_game_form, name='edit_game'),

    #System URLs go here.
    url(r'^systems/$', views.view_systems, name='system-index'),
    url(r'^systems/(?P<system_id>[0-9]+)/$', views.view_system_details, name='system_details'),

    #Company URLs go here.
    url(r'^companies/$', views.view_companies, name='company-index'),
    url(r'^companies/(?P<company_id>[0-9]+)/$', views.view_company_details, name='company_details'),

    #
    url(r'^directors/$', views.view_directors, name='director-index'),
    url(r'^directors/(?P<director_id>[0-9]+)/$', views.view_director_details, name='director_detials'),

    url(r'^publishers/$', views.view_publishers, name='publisher-index'),
    url(r'^publishers/(?P<publisher_id>[0-9]+)/$', views.view_publisher_details, name='publisher_details'),

    url(r'^comments/$', views.view_comments, name='comments-index'),
    url(r'^comments/(?P<comment_id>[0-9]+)/$', views.view_comment_details, name='comment_details'),
    url(r'^comments/create/$', views.create_comment_form, name='create_comment'),

    url(r'^reviews/$', views.view_reviews, name='reviews-index'),
    url(r'^reviews/(?P<review_id>[0-9]+)/$', views.view_review_details, name='review_details'),
    url(r'^reviews/create/$', views.create_review_form, name='create_review'),
    # url(r'^reviews/(?P<review_id>[0-9]+)/edit/$', views.edit_review_form, name='edit_review'),

    url(r'^review_comments/$', views.view_review_comments, name='review_comments-index'),
    url(r'^review_comments/(?P<review_comment_id>[0-9]+)/$', views.view_review_comment_details, name='review_comment_details'),

    url(r'^contact/$', views.contact_form, name='contact_form'),

    ]
