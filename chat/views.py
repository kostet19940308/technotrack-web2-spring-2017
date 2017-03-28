from django.shortcuts import render

from .models  import Chat, Message
from rest_framework import viewsets, permissions
from .serializers import ChatSerializer, MessageSerializer
from .permissions import IsMember

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, IsMember)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super(ChatViewSet, self).get_queryset()
        return queryset.filter(members=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated, IsMember)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super(MessageViewSet, self).get_queryset()
        if 'chat' in self.request.query_params:
            queryset = queryset.filter(chat=self.request.query_params['chat'])
        return queryset