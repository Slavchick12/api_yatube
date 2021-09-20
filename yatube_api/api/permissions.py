from rest_framework import permissions
from rest_framework.permissions import (IsAuthenticatedOrReadOnly)


class AuthorOnly(permissions.BasePermission):
    def has_object_permission(self, view, request, obj):
        if request.action == 'retrieve':
            return [IsAuthenticatedOrReadOnly()]
        return obj.author == view.user
