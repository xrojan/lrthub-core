# Created by Joshua de Guzman on 05/07/2018
# @email code@jmdg.io
from ..models import Feed, FeedType
from .serializers import FeedSerializers
from rest_framework import generics, status
from rest_framework.response import Response


class FeedListApi(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializers

    def list(self, request, *args, **kwargs):
        serializer = FeedSerializers(self.get_queryset(), many=True)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Success", "result": data}
        return Response(response)


class FeedDetailApi(generics.RetrieveAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response = {"status_code": status.HTTP_200_OK, "message": "Success", "result": serializer.data}
        return Response(response)
