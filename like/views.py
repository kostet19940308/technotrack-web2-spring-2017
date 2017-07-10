from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import LikeSerializer
from .permissions import IsFriendsToLike
from .models import Like
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from ugc.models import Post

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated, IsFriendsToLike)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, target_id=self.kwargs["post_id"], target_type=ContentType.objects.get_for_model(Post))

    def get_queryset(self):
        return Like.objects.filter(Q(target_id=self.kwargs["post_id"]) & Q(target_type=ContentType.objects.get_for_model(Post)))