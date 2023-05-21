# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission

# проверка роли модератора
class IsAdmin(BasePermission):

    message = 'Not permissions'

    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        else:
            return False

# проверка является ли автором
class IsAuthor(BasePermission):

    message = 'Not permissions'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True

        else:
            return False


# # проверка является ли владельцем
# class IsOwner(BasePermission):
#
#     message = 'Not permissions'
#
#     def has_object_permission(self, request, view, obj):
#         if request.user == obj.owner:
#             return True
#
#         else:
#             return False
