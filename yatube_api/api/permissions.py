from rest_framework import permissions


class AuthorOnly(permissions.BasePermission):
    def has_object_permission(self, view, request, obj):
        return obj.author == view.user
