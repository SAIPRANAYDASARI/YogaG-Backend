from django.contrib import admin
from .models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'video',
        'created_at',
    )

    search_fields = (
        'user__email',
        'video__title',
    )

    list_filter = (
    "created_at",
    )

    ordering = (
    "-created_at",
    )

    readonly_fields = (
    "created_at",
    )

    list_per_page = 20