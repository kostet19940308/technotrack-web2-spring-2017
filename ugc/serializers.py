from rest_framework import serializers
from .models import Post
from core.serializers import UserSerializer

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'text', 'author')