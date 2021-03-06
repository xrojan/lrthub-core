from django.urls import path
from . import views
from .api import views

urlpatterns = [
    path('', views.FeedList.as_view(), name='api_feed_list'),
    path('all/', views.FeedListAll.as_view(), name='api_feed_list_all'),
    path('<int:pk>/', views.FeedDetail.as_view(), name='api_feed_detail')
]