# Created by Joshua de Guzman on 10/07/2018
# @email code@jmdg.io

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','first_name', 'last_name')
