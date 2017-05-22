from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework import permissions, mixins
from rest_framework.response import Response

from .serializers import UserSerializer, UserAuthorSerializer, UserFriendSerializer
from .models import User
from .permissions import IsOwnerOrReadOnly


class UserListViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    #serializer_class = self.get_user_serializer(self.action)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer(self, *args, **kwargs):
        # user = self.obj
        # request_user = self.request.user
        serializer_class = None
        if self.action == 'list':
            serializer_class = UserAuthorSerializer
        elif self.action == 'retrieve':
            serializer_class = UserFriendSerializer
        else:
            serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


            #def setting(self, request):