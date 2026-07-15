from rest_framework import serializers

from .models import (
    Session,
    SessionVideo,
)

from categories.models import Category


class StartSessionSerializer(serializers.Serializer):

    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(
            is_active=True
        )
    )

class CompleteVideoSerializer(serializers.Serializer):

    session_video = serializers.PrimaryKeyRelatedField(
        queryset=SessionVideo.objects.all()
    )

    watched_duration = serializers.IntegerField(
        min_value=0
    )


class CompleteSessionSerializer(serializers.Serializer):

    session = serializers.PrimaryKeyRelatedField(
        queryset=Session.objects.all()
    )


class SessionVideoSerializer(
    serializers.ModelSerializer
):
    

    class Meta:

        model = SessionVideo

        fields = [
            "id",
            "video",
            "completed",
            "watched_duration",
            "completed_at",
        ]

        read_only_fields = fields
        

class SessionSerializer(
    serializers.ModelSerializer
):
    category = serializers.StringRelatedField()

    session_videos = SessionVideoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Session

        fields = [
            "id",
            "category",
            "total_videos",
            "completed_videos",
            "status",
            "started_at",
            "completed_at",
            "session_videos",
        ]

        read_only_fields = fields