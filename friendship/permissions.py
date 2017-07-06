from rest_framework import permissions
from friendship.models import Friends
from django.db.models import Q


class IsInviterOrRecipient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.is_staff or obj.recipient == request.user

class IsFriends(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.query_params.get('user'):
            friend_id = int(request.query_params.get('user'))
            q = Friends.objects.filter(Q(author_id=request.user.id) & Q(friend_id=friend_id))
            return friend_id == request.user.id or q.exists()
        return True