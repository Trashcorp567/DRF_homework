from rest_framework import permissions
from rest_framework.permissions import BasePermission

from education.models import Subscription


class ModerateCoursesAndLessons(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Менеджер') and request.method not in ['POST', 'DELETE']:
            return True

        if request.user.is_staff:
            return True

        if request.user and request.method in ['GET']:
            return True