from django.contrib import admin
from .models import Session, SessionVideo


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "category",
        "status",
        "total_videos",
        "completed_videos",
        "started_at",
    )

    list_filter = (
        "status",
        "category",
    )

    search_fields = (
    "user__email",
    "category__name",
    )

    readonly_fields = (
    "started_at",
    "completed_at",
    )

    ordering = (
    "-started_at",
    )

    list_per_page = 20


@admin.register(SessionVideo)
class SessionVideoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "session",
        "video",
        "completed",
        "watched_duration",
    )

    list_filter = (
    "completed",
    )

    search_fields = (
    "session__user__email",
    "video__title",
    )

    readonly_fields = (
    "completed_at",
    )

    ordering = (
    "session",
    "video",
    )

    list_per_page = 20