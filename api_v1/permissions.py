from django.http import HttpRequest
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        if request.user and request.user.is_authenticated:
            return request.user.is_superuser
        return request.method in SAFE_METHODS