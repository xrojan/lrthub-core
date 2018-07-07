# Created by Joshua de Guzman on 06/07/2018
# @email code@jmdg.io

from django_filters.rest_framework import DjangoFilterBackend
from ..models import FeedbackConversation, FeedbackMessage
from . import serializers
from . import pagination
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class FeedbackConversationList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FeedbackConversation.objects.all()
    serializer_class = serializers.FeedbackConversationSerializers
    pagination_class = pagination.CustomPagination


class FeedbackConversationCreate(generics.CreateAPIView):
    queryset = FeedbackConversation.objects.all()
    serializer_class = serializers.FeedbackConversationSerializers

    def create(self, request, *args, **kwargs):
        super(FeedbackConversationCreate, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully created", "result": request.data}
        return Response(response)


class FeedbackConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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


class FeedbackMessageList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FeedbackMessage.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = serializers.FeedbackMessageSerializers
    pagination_class = pagination.CustomPagination
    filter_fields = ('conversation_id', 'sender_id',)


class FeedbackMessageCreate(generics.CreateAPIView):
    queryset = FeedbackMessage.objects.all()
    serializer_class = serializers.FeedbackMessageSerializers

    def create(self, request, *args, **kwargs):
        super(FeedbackMessageCreate, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully created", "result": request.data}
        return Response(response)


class FeedbackMessageDetail(generics.RetrieveDestroyAPIView):
    queryset = FeedbackMessage.objects.all()
    serializer_class = serializers.FeedbackMessageSerializers

    def retrieve(self, request, *args, **kwargs):
        super(FeedbackMessageDetail, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully retrieved", "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(FeedbackMessageDetail, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully deleted"}
        return Response(response)
