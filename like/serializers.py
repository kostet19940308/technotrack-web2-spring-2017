from rest_framework import serializers
from .models import Like
from ugc.serializers import UserAuthorSerializer


class LikeSerializer(serializers.ModelSerializer):
    author = UserAuthorSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('author',)
        # read_only_fields = ('target_id', 'target_type')