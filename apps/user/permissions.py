from rest_framework import permissions


class UpdateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user)

class DeleteProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user or request.user.is_staff)