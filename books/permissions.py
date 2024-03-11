from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # uncomment two lines below if I want to allow any authenticated user to update/delete ownerless books
        # if obj.owner == None:
        #     return True
        
        return obj.owner == request.user
    