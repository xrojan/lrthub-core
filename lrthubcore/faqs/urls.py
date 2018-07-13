# Created by Joshua de Guzman on 12/07/2018
# @email code@jmdg.io

from django.urls import path
from . import views
from .api import views as api

urlpatterns = [
    path('', api.FaqList.as_view(), name='api_faq_list'),
    path('list/', views.IndexView.as_view(), name='view_index')
]
