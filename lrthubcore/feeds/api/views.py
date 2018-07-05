# Created by Joshua de Guzman on 05/07/2018
# @email code@jmdg.io
from ..models import Feed, FeedType
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class FeedList(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = serializers.FeedSerializers

    def list(self, request, *args, **kwargs):
        serializer = serializers.FeedSerializers(self.get_queryset(), many=True)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Success", "result": data}
        return Response(response)


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = serializers.FeedSerializers