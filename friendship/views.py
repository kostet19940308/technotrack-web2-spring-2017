from django.shortcuts import render

from rest_framework import serializers, viewsets, permissions, fields
from .models import FriendShip, Friends
from django.db.models import Q
from core.serializers import UserAuthorSerializer
from .serializers import FriendShiptSerializer, FriendsSerializer
from .permissions import IsInviterOrRecipient, IsFriends
from api.permissions import ReadOnly

class FriendShipViewSet(viewsets.ModelViewSet):
    queryset = FriendShip.objects.all()
    serializer_class = FriendShiptSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    permission_classes = (permissions.IsAuthenticated,IsInviterOrRecipient)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, approved=False)

    # def perform_update(self, serializer):
    #     if self.request.user != serializer.validated_data['recipient']:
    #         return
    #     super().perform_update(serializer)

    def get_queryset(self):
        q = self.queryset
        user = self.request.user
        status = self.request.query_params.get('status')
        if status == 'requested':
            q = q.filter(recipient=user, approved=False)
        elif status == 'waiting':
            q = q.filter(author=user, approved=False)
        else:
            q = q.filter(Q(author=user) | Q(recipient=user))
        return q



class FriendsViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer
    permission_classes = (permissions.IsAuthenticated, ReadOnly, IsFriends)

    def get_queryset(self):
        q = self.queryset
        if 'user' in self.request.query_params:
            return q.filter(author=self.request.query_params['user'])
        return q.filter(author=self.request.user)