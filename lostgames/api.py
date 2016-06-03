from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from .models import Game
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class META:
        model = Game
        fields = ('title', 'plot_summary', 'release_date', 'is_shown')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
