from rest_framework import permissions
from .models import ChatMembership
from django.db.models import Q

class IsMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        chat_id = view.kwargs.get('chat_id')
        if chat_id:
            chat_id = int(chat_id)
            return ChatMembership.objects.filter(Q(chat__id = chat_id) & Q(user = request.user)).exists()
        return False

    def has_permission(self, request, view):
        chat_id = view.kwargs.get('chat_id')
        if chat_id:
            chat_id = int(chat_id)
            #print ChatMembership.objects.filter(Q(chat__id = chat_id))
            return ChatMembership.objects.filter(Q(chat__id = chat_id) & Q(user = request.user)).exists()
        return False
