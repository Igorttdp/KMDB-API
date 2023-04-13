from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import Request, View


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )
    

class IsCriticOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user.is_superuser
            or request.user
            and request.user.is_authenticated
            and request.user.is_critic
        )


class CreateUserOrAdmin(BasePermission):
    def has_permission(self, request: Request, view: View):
        return (
            request.method == "POST"
            or request.user
            and request.user.is_authenticated
            and request.user.is_superuser
        )