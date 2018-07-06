# Created by Joshua de Guzman on 07/07/2018
# @email code@jmdg.io

from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('about/', views.CompanyDetail.as_view(), name='api_company_detail'),
]