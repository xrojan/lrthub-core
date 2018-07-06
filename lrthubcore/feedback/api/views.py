# Created by Joshua de Guzman on 06/07/2018
# @email code@jmdg.io

from ..models import FeedbackConversation, FeedbackMessage
from . import serializers
from . import pagination
from rest_framework import generics, status
from rest_framework.response import Response


class FeedbackConversationList(generics.ListCreateAPIView):
    queryset = FeedbackConversation.objects.all()
    serializer_class = serializers.FeedbackConversationSerializers
    pagination_class = pagination.CustomPagination

    def create(self, request, *args, **kwargs):
        super(FeedbackConversationList, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully created", "result": request.data}
        return Response(response)


class FeedbackConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeedbackConversation.objects.all()
    serializer_class = serializers.FeedbackConversationSerializers

    def retrieve(self, request, *args, **kwargs):
        super(FeedbackConversationDetail, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully retrieved", "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(FeedbackConversationDetail, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully updated", "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(FeedbackConversationDetail, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully deleted"}
        return Response(response)
