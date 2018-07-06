# Created by Joshua de Guzman on 07/07/2018
# @email code@jmdg.io

from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.RatingList.as_view(), name='api_rating_list'),
    path('create/', views.RatingCreate.as_view(), name='api_create_list'),
    path('<int:pk>/', views.RatingDetail.as_view(), name='api_detail_list'),
]