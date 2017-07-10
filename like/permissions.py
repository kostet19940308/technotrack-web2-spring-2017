from rest_framework import permissions
from django.db.models import Q
from ugc.models import Post
from friendship.models import Friends

class IsFriendsToLike(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        post_id = view.kwargs.get('post_id')
        if post_id:
            post_id = int(post_id)
            author = Post.objects.get(pk=post_id).author_id
            q = Friends.objects.filter(Q(author_id=request.user.id) & Q(friend_id=author))
            return author == request.user.id or q.exists()
        return False

    def has_permission(self, request, view):
        post_id = view.kwargs.get('post_id')
        if post_id:
            post_id = int(post_id)
            author = Post.objects.get(pk=post_id).author_id
            q = Friends.objects.filter(Q(author_id=request.user.id) & Q(friend_id=author))
            return author == request.user.id or q.exists()
        return False