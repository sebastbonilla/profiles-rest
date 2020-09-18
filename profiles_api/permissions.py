from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # is method is GET it'll e in SAFE_METHODS
        if request.method in permissions.SAFE_METHODS:
            print("here")
            return True

        return obj.id == request.user.id
