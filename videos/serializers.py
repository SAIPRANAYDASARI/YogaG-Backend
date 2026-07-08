from rest_framework import serializers

from .models import (
    Video,
    VideoBenefit,
    VideoStep,
)


class VideoBenefitSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoBenefit
        fields = [
            "id",
            "benefit",
            "order",
        ]


class VideoStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoStep
        fields = [
            "id",
            "step",
            "order",
        ]


class VideoSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    benefits = VideoBenefitSerializer(
        many=True,
        read_only=True,
    )

    steps = VideoStepSerializer(
        many=True,
        read_only=True,
    )

    class Meta:

        model = Video

        fields = [
            "id",
            "title",
            "description",
            "category",
            "video_url",
            "thumbnail",
            "duration",
            "difficulty",
            "focus_area",
            "benefits",
            "steps",
        ]