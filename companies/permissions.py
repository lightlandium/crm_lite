from rest_framework import permissions

class IsCompanyOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'company'):
            company = obj.company
        else:
            company = obj
        return request.user == company.owner

class IsCompanyEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'company'):
            company = obj.company
        else:
            company = obj
        return request.user == company.owner or request.user.company == company