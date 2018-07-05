# Created by Joshua de Guzman on 06/07/2018
# @email code@jmdg.io

from rest_framework import permissions


class IsPostOrIsAuthenticated(permissions.BasePermission):
    """
    Global permission to flag critical updates
    :param: self
    :param: request
    :param: view
    :return: boolean if user is authenticate
    """
    def has_permission(self, request, view):
        # Allows permission from without authentication but requires api key
        # GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # NOTE:
        # Fallthrough if not part of safe methods
        # Protect data to be shared via GET requests (eg. use POST instead)
        # Do not allow updates to the records when not authenticated
        return False
