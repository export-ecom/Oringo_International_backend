# custom_admin/permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUserType(BasePermission):
    """
    Allow access only to users with 'admin' user_type.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'user_type') and request.user.user_type == 'admin'
