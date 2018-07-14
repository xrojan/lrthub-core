# Created by Joshua de Guzman on 15/07/2018
# @email code@jmdg.io

from rest_framework import serializers
from ..models import TrainCheckHistory


class TrainCheckHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainCheckHistory
        fields = ('id', 'no_of_faces', 'no_of_male', 'no_of_female', 'created_on', 'updated_at')
