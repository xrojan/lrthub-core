from django.urls import path
from . import views
from .api import views as api

urlpatterns = [
    # View Routes
    path('', views.FeedList.as_view(), name='feed_list'),
    path('create/', views.FeedCreate.as_view(), name='feed_create'),
    path('<int:pk>', views.FeedDetail.as_view(), name='feed_detail'),
    path('edit/<int:pk>', views.FeedUpdate.as_view(), name='feed_edit'),
    path('delete/<int:pk>', views.FeedDelete.as_view(), name='feed_delete'),
    path('types/', views.FeedTypeList.as_view(), name='feed_type_list'),
    path('types/create/', views.FeedTypeCreate.as_view(), name='feed_type_create'),
    path('types/<int:pk>', views.FeedTypeDetail.as_view(), name='feed_type_detail'),
    path('types/edit/<int:pk>', views.FeedTypeUpdate.as_view(), name='feed_type_edit'),
    path('types/delete/<int:pk>', views.FeedTypeDelete.as_view(), name='feed_type_delete'),

    # API Router
    path('api/', api.FeedList.as_view(), name='api_feed_list'),
    path('api/<int:pk>', api.FeedDetail.as_view(), name='api_feed_detail')
]