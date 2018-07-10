# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class FeedType(models.Model):
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feed(models.Model):
    type_id = models.ForeignKey(FeedType, on_delete=models.PROTECT)
    cover_image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
