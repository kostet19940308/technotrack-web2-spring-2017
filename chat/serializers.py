from .models  import Chat, Message
from rest_framework import serializers
from core.serializers import UserSerializer

class ChatSerializer(serializers.HyperlinkedModelSerializer):

    members = UserSerializer(many=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = ('id','author', 'name', 'members')



class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)
    chat = ChatSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ('author', 'text', 'chat')