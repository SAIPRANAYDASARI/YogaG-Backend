from rest_framework import serializers

from .models import Favorite
from videos.models import Video
from videos.serializers import VideoSerializer

class FavoriteSerializer(serializers.ModelSerializer):

    video = VideoSerializer(read_only=True)

    class Meta:

        model = Favorite

        fields = [
            "id",
            "video",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]

class AddFavoriteSerializer(serializers.Serializer):

    video = serializers.PrimaryKeyRelatedField(
        queryset=Video.objects.filter(is_active=True)
    )