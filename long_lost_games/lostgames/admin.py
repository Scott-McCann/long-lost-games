from django.contrib import admin
from .models import Game, System, Company, Director, Publisher, Comment, Review, Review_Comment
# Register your models here.
admin.site.register(Game)
admin.site.register(System)
admin.site.register(Company)
admin.site.register(Director)
admin.site.register(Publisher)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Review_Comment)
