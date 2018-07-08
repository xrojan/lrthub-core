# Created by Joshua de Guzman on 08/07/2018
# @email code@jmdg.io

from .. import models
from . import serializers
from .pagination import CustomPagination
from rest_framework import generics, status


class AdvertisementList(generics.ListAPIView):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdvertisementSerializer
    pagination_class = CustomPagination
