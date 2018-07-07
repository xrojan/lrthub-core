# Created by Joshua de Guzman on 06/07/2018
# @email code@jmdg.io
from django.contrib.auth.models import User
from rest_framework import serializers

from .. import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class FeedbackConversationSerializers(serializers.ModelSerializer):
    sender = UserSerializer(source='sender_id', many=False, read_only=True)
    receiver = UserSerializer(source='receiver_id', many=False, read_only=True)

    class Meta:
        fields = (
            'id', 'full_name', 'address', 'contact_number', 'employee_name', 'incident_date', 'incident_subject',
            'other_details',
            'is_closed', 'sender', 'sender_id', 'receiver_id', 'receiver', 'created_on', 'updated_at', 'is_deleted',)
        model = models.FeedbackConversation


class FeedbackMessageSerializers(serializers.ModelSerializer):
    conversation = FeedbackConversationSerializers(source='conversation_id', many=False, read_only=True)
    sender = UserSerializer(source='sender_id', many=False, read_only=True)

    class Meta:
        fields = ('id', 'conversation_id', 'conversation', 'sender_id', 'sender', 'message', 'created_on', 'is_deleted')
        model = models.FeedbackMessage
