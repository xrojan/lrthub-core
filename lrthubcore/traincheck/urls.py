# Created by Joshua de Guzman on 15/07/2018
# @email code@jmdg.io

from django.urls import path
from .api import views

urlpatterns = [
    path('', views.TrainCheckList.as_view(), name='api_traincheck_list'),
]