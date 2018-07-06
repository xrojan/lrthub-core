# Created by Joshua de Guzman on 05/07/2018
# @email code@jmdg.io
from ..models import Feed, FeedType
from . import serializers
from . import pagination
from rest_framework import generics, status
from rest_framework.response import Response


class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = serializers.FeedSerializers
    pagination_class = pagination.CustomPagination

    def create(self, request, *args, **kwargs):
        super(FeedList, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully created", "result": request.data}
        return Response(response)


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = serializers.FeedSerializers

    def delete(self, request, *args, **kwargs):
        super(FeedDetail, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully deleted", "result": request.data}
        return Response(response)
