from django.shortcuts import render

from .models  import Chat, Message, ChatMembership
from rest_framework import viewsets, permissions
from .serializers import ChatSerializer, MessageSerializer, ChatMembershipWriteOnlySerializer, ChatMembershipReadOnlySerializer
from .permissions import IsMember
from api.pagination import ResultsSetPagination

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super(ChatViewSet, self).get_queryset()
        return queryset.filter(members=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, IsMember)
    pagination_class = ResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(chat_id=self.kwargs["chat_id"], author=self.request.user)

    def get_queryset(self):
        #queryset = super(MessageViewSet, self).get_queryset()
        return Message.objects.filter(chat_id=self.kwargs["chat_id"])

class ChatMembersViewSet(viewsets.ModelViewSet):
    queryset = ChatMembership.objects.all()
    #serializer_class = ChatMembershipSerializer
    permission_classes = (permissions.IsAuthenticated, IsMember)


    def get_serializer_class(self):
        if self.action == 'create':
            return ChatMembershipWriteOnlySerializer
        return ChatMembershipReadOnlySerializer

    def perform_create(self, serializer):
        #print serializer.user
        serializer.save(chat_id=self.kwargs["chat_id"], inviter=self.request.user)

    def get_queryset(self):
        #q = super(ChatMembersViewSet, self).get_queryset()
        return ChatMembership.objects.filter(chat_id=self.kwargs["chat_id"])
