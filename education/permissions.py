from rest_framework.permissions import BasePermission


class ModerateCoursesAndLessons(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Менеджер') and request.method not in ['POST', 'DELETE']:
            return True

        if request.user.is_staff:
            return True

        return request.user == view.get_object().owner
