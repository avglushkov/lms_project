from rest_framework import permissions

class IsModerator(permissions.BasePermission):
    """ проверка нахождения пользователя в группе модераторов"""

    message = 'User has not permissions for this action'
    def has_permission(self, request, view):
         return request.user.groups.filter(name='moderators').exists()

class IsOwner(permissions.BasePermission):
    """проверка, является ли пользователь владельцем объекта"""

    message = 'User has not permissions for this action'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False

# class IsUsersProfile(permissions.BasePermission):
#     """проверка, является ли профиль профилем пользователя"""
#
#     message = 'Is not your profile. You have not access'
#
#     def has_object_permission(self, request, view, obj):
#         if obj.email == request.user.email:
#             return True
#         else:
#             return False

