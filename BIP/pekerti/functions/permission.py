from rest_framework import permissions

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return request.user.is_staff
        elif view.action == 'destroy':
            return request.user.is_admin
        else:
            return False


class GelombangPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_authenticated
        elif view.action == 'create':
            return request.user.is_authenticated and request.user.is_staff
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return request.user.is_authenticated
        elif view.action in ['update', 'partial_update']:
            return request.user.is_staff
        elif view.action == 'destroy':
            print(request.user.is_staff)
            return request.user.is_staff or request.user.is_superuser
        else:
            return False
