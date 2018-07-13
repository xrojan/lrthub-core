# Created by Joshua de Guzman on 09/07/2018
# @email code@jmdg.io

from django.urls import path
from .api import views

urlpatterns = [
    path('create/', views.UserCreate.as_view(), name='api_user_create')
]