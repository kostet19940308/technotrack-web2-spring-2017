from rest_framework import permissions
from friendship.models import Friends
from django.db.models import Q

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff

class IsFriends(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.query_params.get('author'):
            friend_id = request.query_params.get('author')
        return friend_id == request.user.id or Friends.objects.filter(Q(author=request.user.id) &
                                                                    Q(friend__id = friend_id)).exists()

    def has_permission(self, request, view):
        if request.query_params.get('author'):
            user_id = request.query_params.get('author')
        return user_id == request.user.id or Friends.objects.filter(Q(author=request.user.id) &
                                                                    Q(friend__id = user_id)).exists()