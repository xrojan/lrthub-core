from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class AdvertisementCriteria(models.Model):
    criteria = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.criteria


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    interstitial_image = models.CharField(max_length=255)
    banner_ad_image = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255, blank=True)
    ad_url = models.CharField(max_length=255, blank=True)
    criteria = models.ManyToManyField(AdvertisementCriteria, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
