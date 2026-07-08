from django.urls import path

from .views import SearchVideoAPIView, VideoListAPIView,VideoDetailAPIView,VideosByCategoryAPIView

urlpatterns = [

    path(
        "",
        VideoListAPIView.as_view(),
        name="video-list",
    ),
    path(
        "<int:pk>/",
        VideoDetailAPIView.as_view(),
        name="video-detail",
    ),
    path(
        "category/<int:category_id>/",
        VideosByCategoryAPIView.as_view(),
        name="videos-by-category",
    ),
    path(
        "search/",
        SearchVideoAPIView.as_view(),
        name="video-search",
    ),

]