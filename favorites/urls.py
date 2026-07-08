from django.urls import path

from .views import (
    AddFavoriteAPIView,
    ListFavoritesAPIView,
    RemoveFavoriteAPIView,
)

urlpatterns = [

    path(
        "",
        AddFavoriteAPIView.as_view(),
        name="add-favorite",
    ),

    path(
        "list/",
        ListFavoritesAPIView.as_view(),
        name="list-favorites",
    ),

    path(
        "<int:video_id>/",
        RemoveFavoriteAPIView.as_view(),
        name="remove-favorite",
    ),

]