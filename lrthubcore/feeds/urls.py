from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedList.as_view(), name='feed_list'),
    path('create/', views.FeedCreate.as_view(), name='feed_create'),
    path('<int:pk>', views.FeedDetail.as_view(), name='feed_view'),
    path('edit/<int:pk>', views.FeedUpdate.as_view(), name='feed_update'),
    path('delete/<int:pk', views.FeedDelete.as_view(), name='feed_delete')
]