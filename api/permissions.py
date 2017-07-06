from rest_framework import permissions
from friendship.models import Friends
from django.db.models import Q

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff

class ReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class IsContentOfFriends(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # friend_id = int(view.kwargs['user_id'])
        # q = Friends.objects.filter(Q(author_id=request.user.id) & Q(friend_id=friend_id))
        # return friend_id == request.user.id or q.exists()
        friend_id = obj.author.id
        #print friend_id
        if friend_id is not None:
            #friend_id = request.query_params.get('author')
            q = Friends.objects.filter(Q(author_id=request.user.id) & Q(friend_id=friend_id))
            #print q
            return friend_id == request.user.id or q.exists()
        return False

    def has_permission(self, request, view):
        if request.query_params.get('author'):
            friend_id = int(request.query_params.get('author'))
            q = Friends.objects.filter(Q(author_id=request.user.id) & Q(friend_id=friend_id))
            return friend_id == request.user.id or q.exists()
        return True