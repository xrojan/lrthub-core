# Created by Joshua de Guzman on 08/07/2018
# @email code@jmdg.io

from ..models import Advertisement, AdvertisementCriteria
from rest_framework import serializers


class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementCriteria
        fields = ('id', 'criteria',)


class AdvertisementSerializer(serializers.ModelSerializer):
    criteria = CriteriaSerializer(many=True, read_only=True)

    class Meta:
        model = Advertisement
        fields = (
        'id', 'description', 'interstitial_image', 'banner_ad_image', 'video_url', 'criteria', 'ad_url', 'created_on',
        'updated_at',
        'is_deleted')
