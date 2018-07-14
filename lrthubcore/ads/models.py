from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.CharField(max_length=255)
    cover_image = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255, blank=True)
    view_hits = models.BigIntegerField(default=0, )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class AdvertisementPreferenceCriteria(models.Model):
    criteria = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.criteria


class AdvertisementCriteria(models.Model):
    ad_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    pref_id = models.ForeignKey(AdvertisementPreferenceCriteria, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.ad_id, self.pref_id)


class AdvertisementUserPreference(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pref_id = models.ForeignKey(AdvertisementPreferenceCriteria, on_delete=models.CASCADE)
    is_enabled = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.user_id, self.pref_id)
