from rest_framework import permissions
from friendship.models import Friends
from django.db.models import Q


class IsInviterOrRecipient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff or obj.recipient == request.user