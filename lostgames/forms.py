from django import forms
from .models import Game, Review, Comment

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField()

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['category', 'title','release_date','systems','director','is_shown']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'review_text', 'user', 'likes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['game', 'comment_text', 'user', 'likes']

# class ModCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['game', 'comment_text', 'user', 'likes']
