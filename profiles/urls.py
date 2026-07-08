from django.urls import path

from .views import ViewProfileAPIView,UpdateProfileAPIView

urlpatterns = [

    path(
        "",
        ViewProfileAPIView.as_view(),
        name="view-profile",
    ),

    path(
        "update/",
        UpdateProfileAPIView.as_view(),
        name="update-profile",
    ),

]