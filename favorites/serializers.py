from rest_framework import serializers
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    video_title = serializers.CharField(
        source='video.title',
        read_only=True
    )

    class Meta:
        model = Favorite
        fields = [
            'id',
            'video',
            'video_title',
            'created_at'
        ]
        read_only_fields = [
            'id',
            'created_at'
        ]