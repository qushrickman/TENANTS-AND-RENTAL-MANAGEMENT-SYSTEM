from rest_framework.permissions import BasePermission

class IsLandlord(BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role == 'LANDLORD'


class IsTenant(BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.role == 'TENANT'
