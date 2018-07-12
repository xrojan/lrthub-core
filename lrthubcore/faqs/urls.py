# Created by Joshua de Guzman on 12/07/2018
# @email code@jmdg.io

from django.urls import path
from .api import views

urlpatterns = [
    path('', views.FaqList.as_view(), name='api_faq_list'),
]
