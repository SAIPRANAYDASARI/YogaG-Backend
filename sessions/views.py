from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db import transaction

from .models import (
    Session,
    SessionVideo,
)

from django.utils import timezone

from .serializers import (
    StartSessionSerializer,
    SessionSerializer,
    CompleteVideoSerializer,
    CompleteSessionSerializer,
)

from videos.models import Video

class StartSessionAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = StartSessionSerializer(
            data=request.data
        )

        if serializer.is_valid():

            category = serializer.validated_data["category"]

            videos = Video.objects.filter(
                category=category,
                is_active=True,
            ).order_by("order")

            video_count = videos.count()

            if video_count == 0:

                return Response(
                    {
                        "success": False,
                        "message": "No videos available for this category.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            with transaction.atomic():

                session = Session.objects.create(
                    user=request.user,
                    category=category,
                    total_videos=video_count,
                )

                session_videos = [

                    SessionVideo(
                        session=session,
                        video=video,
                    )

                    for video in videos
                ]

                SessionVideo.objects.bulk_create(
                    session_videos
                )

            response_serializer = SessionSerializer(
                session
            )

            return Response(
                {
                    "success": True,
                    "message": "Session started successfully.",
                    "data": response_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class CompleteVideoAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CompleteVideoSerializer(
            data=request.data
        )

        if serializer.is_valid():

            session_video = serializer.validated_data["session_video"]

            if session_video.session.user != request.user:

                return Response(
                    {
                        "success": False,
                        "message": "Permission denied.",
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

            if session_video.completed:

                return Response(
                    {
                        "success": False,
                        "message": "Video already completed.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            session_video.completed = True

            session_video.watched_duration = serializer.validated_data[
                "watched_duration"
            ]

            session_video.completed_at = timezone.now()

            session_video.save(
                update_fields=[
                    "completed",
                    "watched_duration",
                    "completed_at",
                ]
            )

            session = session_video.session

            session.completed_videos +=1
           

            session.save(
                update_fields=[
                    "completed_videos",
                ]
            )

            return Response(
                {
                    "success": True,
                    "message": "Video marked as completed.",
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class CompleteSessionAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CompleteSessionSerializer(
            data=request.data
        )

        if serializer.is_valid():

            session = serializer.validated_data["session"]

            if session.user != request.user:

                return Response(
                    {
                        "success": False,
                        "message": "Permission denied."
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

            remaining = session.session_videos.filter(
                completed=False
            ).exists()

            if remaining:

                return Response(
                    {
                        "success": False,
                        "message": "Complete all videos before finishing the session."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            if session.status == "COMPLETED":

                return Response(
                    {
                        "success": False,
                        "message": "Session already completed."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            session.status = "COMPLETED"

            session.completed_at = timezone.now()

            session.save(
                update_fields=[
                    "status",
                    "completed_at",
                ]
            )

            return Response(
                {
                    "success": True,
                    "message": "Session completed successfully."
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
class SessionHistoryAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        sessions = Session.objects.filter(
            user=request.user
        ).prefetch_related(
            "session_videos"
        ).select_related(
            "category"
        )

        serializer = SessionSerializer(
            sessions,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": sessions.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )