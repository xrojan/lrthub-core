# Created by Joshua de Guzman on 05/07/2018
# @email code@jmdg.io

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Appends status code the base exception result
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['message'] = response.data['detail']
        del response.data['detail']

    return response
