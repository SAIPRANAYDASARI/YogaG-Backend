from django.contrib import admin
from .models import Video, VideoBenefit, VideoStep


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'difficulty',
        'duration',
        'is_active',
    )

    search_fields = (
        'title',
        'focus_area',
    )

    list_filter = (
        'category',
        'difficulty',
        'is_active',
    )

    ordering = (
        'category',
        'order',
    )


@admin.register(VideoBenefit)
class VideoBenefitAdmin(admin.ModelAdmin):

    list_display = (
        'video',
        'order',
    )


@admin.register(VideoStep)
class VideoStepAdmin(admin.ModelAdmin):

    list_display = (
        'video',
        'order',
    )