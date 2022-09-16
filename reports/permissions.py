from rest_framework.permissions import BasePermission, SAFE_METHODS


class isPermittedDonor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.methods in SAFE_METHODS:
            return True
        return obj.donor == request.user


class centerIsPermitted(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.methods in SAFE_METHODS:
            return True
        return obj.donation_center == request.user