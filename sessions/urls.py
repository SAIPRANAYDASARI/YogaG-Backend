from django.urls import path

from .views import CompleteSessionAPIView, StartSessionAPIView,CompleteVideoAPIView,SessionHistoryAPIView

urlpatterns = [

    path(
        "start/",
        StartSessionAPIView.as_view(),
        name="start-session",
    ),

    path(
        "video/complete/",
        CompleteVideoAPIView.as_view(),
        name="complete-video",
    ),

    path(
        "complete/",
        CompleteSessionAPIView.as_view(),
        name="complete-session",
    ),

    path(
        "history/",
        SessionHistoryAPIView.as_view(),
        name="session-history",
    ),

]