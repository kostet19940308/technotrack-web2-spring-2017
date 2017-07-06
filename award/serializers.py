from rest_framework import serializers, viewsets, permissions, fields
from .models import Award
from core.serializers import UserAuthorSerializer

class AwardSerializer(serializers.ModelSerializer):
    author = UserAuthorSerializer()

    class Meta:
        model = Award
        fields = ('author', 'title', 'text')

