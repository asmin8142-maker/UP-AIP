from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Доступ только владельцу объекта.
    """

    message = 'У вас нет прав для доступа к этому объекту.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user