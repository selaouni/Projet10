from rest_framework.permissions import BasePermission
from rest_framework import permissions



class BasePermission(BasePermission):
    """
    A base class from which all permission classes should inherit.
    """

    edit_methods = ("PUT", "PATCH")

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return True

    # def has_object_permission(self, request, view, obj):
    #     # if request.user.is_superuser:
    #     #     return True
    #
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     if obj.author == request.user:
    #         return True
    #
    #     if request.user.is_staff and request.method not in self.edit_methods:
    #         return True
    #
    #     return False


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author_user_id == request.user


class IsStaffpermission(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        user = request.user
        if user.has_perm('project.view_project'):
                return True
        if user.has_perm('project.add_project'):
                return True
        return False