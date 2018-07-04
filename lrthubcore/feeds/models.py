# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Feed(models.Model):
    type_id = models.IntegerField()
    cover_image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
