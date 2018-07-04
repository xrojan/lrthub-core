# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Feed


# Create your views here.
class FeedList(ListView):
    model = Feed


class FeedVied(DetailView):
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
