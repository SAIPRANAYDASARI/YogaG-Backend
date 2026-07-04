from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer


class VideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(is_active=True)


class VideoDetailView(generics.RetrieveAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.filter(is_active=True)