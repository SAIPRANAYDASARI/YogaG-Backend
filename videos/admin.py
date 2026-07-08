from django.contrib import admin

from .models import (
    Video,
    VideoBenefit,
    VideoStep,
)


class VideoBenefitInline(admin.TabularInline):
    model = VideoBenefit
    extra = 1


class VideoStepInline(admin.TabularInline):
    model = VideoStep
    extra = 1


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "category",
        "difficulty",
        "duration",
        "is_active",
    )

    list_filter = (
        "category",
        "difficulty",
        "is_active",
    )

    search_fields = (
        "title",
        "focus_area",
    )

    inlines = [
        VideoBenefitInline,
        VideoStepInline,
    ]