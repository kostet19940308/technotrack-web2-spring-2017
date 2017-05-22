from .models  import Chat, Message
from rest_framework import serializers
from core.serializers import UserAuthorSerializer

class ChatSerializer(serializers.HyperlinkedModelSerializer):

    members = UserAuthorSerializer(many=True)
    author = UserAuthorSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = ('id','author', 'name', 'members')



class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = UserAuthorSerializer(read_only=True)
    chat = ChatSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ('author', 'text', 'chat')