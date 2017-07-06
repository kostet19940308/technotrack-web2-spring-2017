# from .models  import Feed
# from generic_relations.relations import GenericRelatedField
# from rest_framework import serializers, viewsets
# from application.api import router
# from ugc.models import Post
# from ugc.apy import PostSerializer, CommentSerializer
# from message.api import MessageSerializer, ChatSerializer
# from like.api import LikeSerializer
# from like.models import Like
# from core.api import UserSerializer
# from django.contrib.contenttypes.models import ContentType
# from rest_framework.reverse import reverse
#
#
# class FeedSerializer(serializers.HyperlinkedModelSerializer):
#     content_object = GenericRelatedField({
#         Achieve: AchieveSerializer(read_only=True, allow_null=True),
#         Friendship: FriendshipSerializer(read_only=True, allow_null=True),
#         Post: PostSerializer(read_only=True),
#     })
#     # content_type = fields.CharField(read_only=True)
#     content_type = fields.SerializerMethodField('get_event_type')
#
#     created = serializers.DateTimeField(read_only=True, format='%X %d %b %Y')
#     author = UserSerializer()
#
#     class Meta:
#         model = Event
#         fields = ('id', 'author', 'created', 'title', 'content_object', 'content_type')
#         # exclude = ('content_object',)
#         depth = 0
#
#     def get_event_type(self, obj):
#         # print(ContentTypeManager().get_for_model(obj), dir(ContentTypeManager().get_for_model(obj)))
#         content_object_name = str(type(obj.content_object)).replace('\'>','').split('.')
#         return content_object_name[len(content_object_name) - 1]
#
# class EventViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#
#     def get_queryset(self):
#         queryset = super(EventViewSet, self).get_queryset()
#         #queryset = queryset.filter(author=self.request.user)
#         return queryset