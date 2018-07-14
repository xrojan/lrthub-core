# Created by Joshua de Guzman on 14/07/2018
# @email code@jmdg.io

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class CustomPagination(PageNumberPagination):
    """
    Adds pagination links to list requests
    Class is made to override get_paginated_response() pagination serializer with custom pagination styles
    Declared variables can also be set when pagination class is called with instance
    :param: page_size: Default is 10
    :type: page_size: int
    :param: page_size_query_param: Default is 'page_size
    :type: page_size_query_param: String
    :param: max_page_size: Default is 1000
    :type: max_page_size: int
    :return: Returns formatted list request response with nav links and counts
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'status_code': status.HTTP_200_OK,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_count': self.page.paginator.num_pages,
            'results': data
        })
