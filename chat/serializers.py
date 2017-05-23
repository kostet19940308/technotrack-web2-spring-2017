from .models  import Chat, Message, ChatMembership
from rest_framework import serializers
from core.serializers import UserAuthorSerializer
from django.db.models import Q

class ChatSerializer(serializers.HyperlinkedModelSerializer):

    members = UserAuthorSerializer(many=True)
    author = UserAuthorSerializer(read_only=True)
    last_message = serializers.SerializerMethodField('get_message')

    class Meta:
        model = Chat
        fields = ('id','author', 'name', 'members', 'last_message')

    def get_message(self, obj):
        last_message = obj.messages.all().order_by('-created_at')[0]
        return {
            'author': last_message.author.username,
            'text': last_message.text,
        }


class ChatAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id','name')




class MessageSerializer(serializers.HyperlinkedModelSerializer):
    author = UserAuthorSerializer(read_only=True)
    chat = ChatAuthorSerializer()
    class Meta:
        model = Message
        fields = ('author', 'title', 'text', 'chat', 'created_at')




class ChatMembershipReadOnlySerializer(serializers.ModelSerializer):
    user = UserAuthorSerializer(read_only=True)
    chat = ChatAuthorSerializer( read_only=True)
    created = serializers.ReadOnlyField(source='created_at', read_only=True)
    inviter = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ChatMembership
        fields = ('user', 'chat', 'inviter', 'created')


class ChatMembershipWriteOnlySerializer(serializers.ModelSerializer):
    #user_id = serializers.PrimaryKeyRelatedField(read_only=True, source='user.id')
    inviter = serializers.PrimaryKeyRelatedField(read_only=True)
    chat_id = serializers.PrimaryKeyRelatedField(read_only=True, source='chat.id')

    class Meta:
        model = ChatMembership
        fields = ('user', 'inviter', 'chat_id')