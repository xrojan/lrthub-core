# Created by Joshua de Guzman on 06/07/2018
# @email code@jmdg.io
from django.contrib.auth.models import User
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from ..models import FeedbackConversation, FeedbackMessage
from . import serializers
from . import pagination
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class FeedbackConversationList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.FeedbackConversationSerializers
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        """
        Only allows user to view their feedback conversation with the receiver
        which is currently set to the administrators
        :return: Filtered feedback conversations
        """
        queryset = FeedbackConversation.objects.all()
        user = self.request.user
        return queryset.filter(sender_id=user)


class FeedbackConversationCreate(generics.CreateAPIView):
    queryset = FeedbackConversation.objects.all()
    serializer_class = serializers.FeedbackConversationSerializers

    def create(self, request, *args, **kwargs):
        """
        Validates creation of conversations
        Only allows to send messages to an existing user and also an administration staff, validates sender id with the request's authentication user
        """
        user = self.request.user
        request_sender_id = int(request.POST.get('sender_id', ''))
        request_receiver_id = int(request.POST.get('receiver_id', ''))

        # Validate if receiver is existing and is a staff
        user_staff = get_object_or_404(User, pk=request_receiver_id)
        if user_staff.is_staff is not True:
            response = {"status_code": status.HTTP_403_FORBIDDEN,
                        "message": "Not allowed to continue with the action", "result": None}
            return Response(response)

        # Validate if the authentication request is equal to the sender_id
        elif user.id == request_sender_id:
            super(FeedbackConversationCreate, self).create(request, args, kwargs)
            response = {"status_code": status.HTTP_201_CREATED,
                        "message": "Successfully created",
                        "result": request.data}
            return Response(response)
        else:
            response = {"status_code": status.HTTP_403_FORBIDDEN,
                        "message": "You are not allowed to create the requested conversation",
                        "result": None}
            return Response(response)


class FeedbackConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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

    def get_queryset(self):
        """
        Only allows user to view their feedback conversation with the receiver
        which is currently set to the administrators
        :return: Filtered feedback conversations
        """
        queryset = FeedbackConversation.objects.all()
        user = self.request.user
        return queryset.filter(sender_id=user)


class FeedbackMessageList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = FeedbackMessage.objects.all()
    filter_backends = (DjangoFilterBackend,)
    serializer_class = serializers.FeedbackMessageSerializers
    pagination_class = pagination.CustomPagination
    filter_fields = ('conversation_id', 'sender_id',)

    def get_queryset(self):
        """
        Only allows user to view their feedback messages in a conversation if they are member of it
        which is currently set to the administrators
        :return: Filtered feedback conversation messages
        """
        queryset = FeedbackMessage.objects.all()
        user = self.request.user
        query = Q(sender_id=user)
        query.add(Q(receiver_id=user), Q.OR)
        return queryset.filter(query)


class FeedbackMessageCreate(generics.CreateAPIView):
    queryset = FeedbackMessage.objects.all()
    serializer_class = serializers.FeedbackMessageSerializers

    def create(self, request, *args, **kwargs):
        """
        Validates creation of messages
        Only authorizes users that are part of the conversation to create message
        """
        user = self.request.user
        request_receiver_id = int(request.POST.get('receiver_id', ''))
        request_sender_id = int(request.POST.get('sender_id', ''))
        conversations = get_object_or_404(FeedbackConversation, pk=request.POST.get('conversation_id', ''))
        if conversations.sender_id == user or conversations.receiver_id == user:
            if (
                    conversations.sender_id_id == request_sender_id and conversations.receiver_id_id == request_receiver_id) or (
                    conversations.sender_id_id == request_receiver_id and conversations.receiver_id_id == request_sender_id):
                super(FeedbackMessageCreate, self).create(request, args, kwargs)
                response = {"status_code": status.HTTP_200_OK, "message": "Successfully created",
                            "result": request.data}
                return Response(response)
            else:
                response = {"status_code": status.HTTP_403_FORBIDDEN,
                            "message": "Invalid users for the conversation",
                            "result": None}
                return Response(response)
        else:
            response = {"status_code": status.HTTP_403_FORBIDDEN, "message": "You are not part of this conversation",
                        "result": None}
            return Response(response)


class FeedbackMessageDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
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

    def get_queryset(self):
        """
        Only allows user to view their feedback messages in a conversation if they are member of it
        which is currently set to the administrators
        :return: Filtered feedback conversation messages
        """
        queryset = FeedbackMessage.objects.all()
        user = self.request.user
        query = Q(sender_id=user)
        query.add(Q(receiver_id=user), Q.OR)
        return queryset.filter(query)
