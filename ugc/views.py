from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from api.permissions import IsOwnerOrReadOnly
#from django.utils import timezone

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        q = super(PostViewSet, self).get_queryset()
        if self.request.query_params.get('author'):
            print self.request.query_params.get('author')
            q = q.filter(author=self.request.query_params.get('author'))
        return q