from django.contrib import admin

from .models import (
    Video,
    VideoBenefit,
    VideoStep,
)


class VideoBenefitInline(admin.TabularInline):
    model = VideoBenefit
    extra = 1
    ordering = ("order",)


class VideoStepInline(admin.TabularInline):
    model = VideoStep
    extra = 1
    ordering = ("order",)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "category",
        "difficulty",
        "duration",
        "order",
        "is_active",
    )

    list_filter = (
        "category",
        "difficulty",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "focus_area",
    )

    ordering = (
        "category",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        VideoBenefitInline,
        VideoStepInline,
    ]

    list_per_page = 20

    