# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Feed, FeedType
from django.contrib import admin

# Register your models here.
admin.site.register(FeedType)
admin.site.register(Feed)
