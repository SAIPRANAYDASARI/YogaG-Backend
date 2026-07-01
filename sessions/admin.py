from django.contrib import admin
from .models import Session, SessionVideo


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'category',
        'status',
        'started_at',
    )

    list_filter = (
        'status',
    )


@admin.register(SessionVideo)
class SessionVideoAdmin(admin.ModelAdmin):

    list_display = (
        'session',
        'video',
        'completed',
    )