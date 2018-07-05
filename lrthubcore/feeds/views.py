# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Feed, FeedType


# Create your views here.
class FeedList(ListView):
    model = Feed


class FeedDetail(DetailView):
    model = Feed


class FeedCreate(CreateView):
    model = Feed
    fields = ['type_id', 'cover_image', 'title', 'content', 'is_deleted']
    success_url = reverse_lazy('feed_list')


class FeedUpdate(UpdateView):
    model = Feed
    fields = ['type_id', 'cover_image', 'title', 'content', 'is_deleted']
    success_url = reverse_lazy('feed_list')


class FeedDelete(DeleteView):
    model = Feed
    success_url = reverse_lazy('feed_list')


class FeedTypeList(ListView):
    model = FeedType
    template_name = 'types/feed_type_list.html'


class FeedTypeDetail(DetailView):
    model = FeedType
    template_name = 'types/feed_type_detail.html'


class FeedTypeCreate(CreateView):
    model = FeedType
    template_name = 'types/feed_type_form.html'
    fields = ['name']
    success_url = reverse_lazy('feed_type_list')


class FeedTypeUpdate(UpdateView):
    model = FeedType
    template_name = 'types/feed_type_form.html'
    fields = ['name']
    success_url = reverse_lazy('feed_type_list')


class FeedTypeDelete(DeleteView):
    model = FeedType
    template_name = 'types/feed_type_confirm_delete.html'
    success_url = reverse_lazy('feed_type_list')
