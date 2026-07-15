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

        read_only_fields = fields


class VideoStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoStep
        fields = [
            "id",
            "step",
            "order",
        ]

        read_only_fields = fields


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
            # Basic information 

            "id",
            "title",
            "description",
            "category",

            #Media

            "video_url",
            "thumbnail",

            #Yoga Details


            "duration",
            "difficulty",
            "focus_area",

            #Related Data

            
            "benefits",
            "steps",
        ]

        read_only_fields = fields