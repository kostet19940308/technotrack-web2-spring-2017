from rest_framework import serializers
from .models import Post
from core.serializers import UserAuthorSerializer

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserAuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'text', 'author')