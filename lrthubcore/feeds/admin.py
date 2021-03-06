# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Feed, FeedType
from django.contrib import admin


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    search_fields = ['type_id__name', 'title', 'content', ]
    list_display = ('type_id', 'title', 'content')
    list_filter = ('type_id', 'is_deleted',)


class FeedAdminInline(admin.TabularInline):
    model = Feed
    fields = ('title', 'content',)
    readonly_fields = ('title', 'content',)


@admin.register(FeedType)
class FeedTypeAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_on'
    search_fields = ['name', ]
    inlines = (FeedAdminInline,)
    list_display = ('name', 'feed_count', 'is_on_main_page', 'created_on', 'updated_at')
    list_filter = ('is_deleted',)

    # noinspection PyMethodMayBeStatic
    def feed_count(self, obj):
        return obj.feed_set.count()
