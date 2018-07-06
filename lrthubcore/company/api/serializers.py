# Created by Joshua de Guzman on 07/07/2018
# @email code@jmdg.io

from ..models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'vision', 'mission', 'cover_image', 'contact_description')
        model = Company
