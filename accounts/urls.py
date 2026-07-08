from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    ForgotPasswordAPIView,
    ResetPasswordAPIView,
)
urlpatterns = [
    path(
        "register/",
        RegisterAPIView.as_view(),
        name="register",
    ),

    path(
        "login/",
        LoginAPIView.as_view(),
        name="login",
    ),

    path(
    "logout/",
    LogoutAPIView.as_view(),
    name="logout",
),

    path(
    "forgot-password/",
    ForgotPasswordAPIView.as_view(),
    name="forgot-password",
),

    path(
    "reset-password/",
    ResetPasswordAPIView.as_view(),
    name="reset-password",
),


]