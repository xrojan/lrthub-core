# Created by Joshua de Guzman on 12/07/2018
# @email code@jmdg.io

from ..models import Faq
from rest_framework import serializers


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('question', 'answer',)
