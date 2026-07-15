from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "gender",
        "fitness_level",
        "height",
        "weight",
    )

    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    list_filter = (
    "gender",
    "fitness_level",
    )

    readonly_fields = (
    "created_at",
    "updated_at",
    )

    ordering = (
    "user",
    )

    list_per_page = 20