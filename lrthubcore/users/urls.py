# Created by Joshua de Guzman on 09/07/2018
# @email code@jmdg.io

from django.urls import path
from .api import views

urlpatterns = [
    path('create/', views.UserCreate.as_view(), name='api_user_create'),
    path('profile/', views.UserProfileList.as_view(), name='api_user_list'),
    path('profile/<int:pk>/', views.UserProfileDetail.as_view(), name='api_user_detail'),
    path('profile/options/gender/', views.UserProfileGenderList.as_view(), name='api_gender_list'),
    path('profile/options/nationality/', views.UserProfileNationalityList.as_view(), name='api_nationality_list'),
    path('profile/options/marital-status/', views.UserProfileMaritalStatusList.as_view(), name='api_marital_status_list'),
    path('profile/options/employment-type/', views.UserProfileEmploymentTypeList.as_view(), name='api_employment_type_list'),
    path('profile/options/disabilities/', views.UserProfileDisabilityList.as_view(), name='api_disabilities_list'),
]