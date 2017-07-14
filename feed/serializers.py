from .models import Feed
from rest_framework import serializers, viewsets
from ugc.models import Post
from ugc.serializers import PostSerializer
from friendship.models import Friends
from friendship.serializers import FriendsSerializer
from award.models import Award
from award.serializers import AwardSerializer
from core.serializers import UserAuthorSerializer
from django.contrib.contenttypes.models import ContentType
from rest_framework.reverse import reverse


class TaggedObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        """
        Serialize bookmark instances using a bookmark serializer,
        and note instances using a note serializer.
        """
        if isinstance(value, Post):
            serializer = PostSerializer(value)
        elif isinstance(value, Friends):
            serializer = FriendsSerializer(value)
        elif isinstance(value, Award):
            serializer = AwardSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    #content_object = TaggedObjectRelatedField(read_only=True)

    created_at = serializers.DateTimeField(read_only=True, format='%X %d %b %Y')
    author = UserAuthorSerializer()

    class Meta:
        model = Feed
        fields = ('id', 'author', 'text', 'created_at')
        depth = 0