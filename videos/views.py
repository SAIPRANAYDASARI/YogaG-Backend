from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video
from .serializers import VideoSerializer

class VideoListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        videos = Video.objects.filter(
            is_active=True
        ).select_related(
            "category"
        ).prefetch_related(
            "benefits",
            "steps",
        )
        

        serializer = VideoSerializer(
            videos,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": videos.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    



class VideoDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        video = get_object_or_404(
            Video.objects.select_related(
                "category"
            ).prefetch_related(
                "benefits",
                "steps",
            ),
            pk=pk,
            is_active=True,
        )

        serializer = VideoSerializer(video)

        return Response(
            {
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    
class VideosByCategoryAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, category_id):

        videos = (
            Video.objects.filter(
            category_id=category_id,
            is_active=True,
        ).select_related("category")
         .prefetch_related("benefits","steps")
        )

        serializer = VideoSerializer(
            videos,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": videos.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    
