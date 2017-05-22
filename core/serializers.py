from rest_framework import serializers, fields
from .models import User


class UserAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username')


class UserFriendSerializer(serializers.ModelSerializer):
    id = fields.ReadOnlyField
    username = fields.ReadOnlyField()
    status = fields.SerializerMethodField('get_status_to_friends')
    about_yourself = fields.SerializerMethodField('get_about_yourself_to_friends')
    class Meta:
        model = User
        fields = ('id', "username", "last_name", "first_name", "status", "about_yourself")

    def get_status_to_friends(self, obj):
        request = self.context['request']
        if obj.friend.filter(friend__id=request.user.id).exists() or request.user.is_staff or obj == request.user:
            return obj.status
        return None

    def get_about_yourself_to_friends(self, obj):
        request = self.context['request']
        if obj.friend.filter(friend__id=request.user.id).exists() or request.user.is_staff or obj == request.user:
            return obj.about_yourself
        return None

class UserSerializer(serializers.ModelSerializer):
    id = fields.ReadOnlyField
    username = fields.ReadOnlyField()
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='api:users-detail',
    #     lookup_url_kwarg='user_id',
    #     lookup_field='pk'
    # )

    class Meta:
        model = User
        fields = ('id', "username", "last_name", "first_name", "status", "about_yourself")