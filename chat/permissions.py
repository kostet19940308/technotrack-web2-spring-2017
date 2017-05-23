from rest_framework import permissions
from .models import ChatMembership
from django.db.models import Q

class IsMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        chat_id = int(view.kwargs['chat_id'])
        return ChatMembership.objects.filter(Q(chat__id = chat_id) & Q(user = request.user)).exists()

    def has_permission(self, request, view):
        chat_id = int(view.kwargs['chat_id'])
        return ChatMembership.objects.filter(Q(chat__id = chat_id) & Q(user = request.user)).exists()