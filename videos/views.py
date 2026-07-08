from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video
from .serializers import VideoSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q

class VideoListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        videos = Video.objects.filter(
            is_active=True
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
            Video,
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

        videos = Video.objects.filter(
            category_id=category_id,
            is_active=True,
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
    
class SearchVideoAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        query = request.GET.get("q", "").strip()

        videos = Video.objects.filter(
            is_active=True
        )

        if query:

            videos = videos.filter(

                Q(title__icontains=query)

                |

                Q(description__icontains=query)

                |

                Q(focus_area__icontains=query)

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
