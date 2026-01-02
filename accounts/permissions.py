from rest_framework.permissions import BasePermission

class Roles:
    LANDLORD = "LANDLORD"
    TENANT = "TENANT"
class IsLandlord(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.profile.Role == "LANDLORD"
        )


class IsTenant(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.profile.Role == "TENANT"
        )
