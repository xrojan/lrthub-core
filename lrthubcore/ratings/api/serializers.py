# Created by Joshua de Guzman on 07/07/2018
# @email code@jmdg.io

from ..models import Rating
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_id', many=False, read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'user_id', 'user', 'value', 'created_on', 'updated_at', 'is_deleted')
