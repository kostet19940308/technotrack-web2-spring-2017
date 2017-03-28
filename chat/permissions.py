from rest_framework import permissions

class IsMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user in obj.members.all():
            return True
        return request.user.is_staff