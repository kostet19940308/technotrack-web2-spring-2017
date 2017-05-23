from rest_framework import serializers, viewsets, permissions, fields
from .models import FriendShip, Friends
from core.serializers import UserAuthorSerializer


class FriendShiptSerializer(serializers.ModelSerializer):
    author = UserAuthorSerializer(read_only=True)
    #recipient = UserAuthorSerializer()

    class Meta:
        model = FriendShip
        fields = ('id','author', 'recipient', 'approved',)


class FriendsSerializer(serializers.ModelSerializer):
    friend = UserAuthorSerializer()

    class Meta:
        model = Friends
        fields = ['friend', ]