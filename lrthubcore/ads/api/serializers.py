# Created by Joshua de Guzman on 08/07/2018
# @email code@jmdg.io

from ..models import Advertisement
from rest_framework import serializers


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('id', 'description', 'interstitial_image', 'banner_ad_image', 'video_url', 'created_on', 'updated_at',
                  'is_deleted')
