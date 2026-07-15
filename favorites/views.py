from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



from .models import Favorite
from .serializers import (
    AddFavoriteSerializer,
    FavoriteSerializer,
)
from videos.models import Video


class AddFavoriteAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = AddFavoriteSerializer(
            data=request.data
        )

        if serializer.is_valid():

            video = serializer.validated_data["video"]

            favorite, created = Favorite.objects.get_or_create(
                user=request.user,
                video=video,
            )

            if not created:

                return Response(
                    {
                        "success": False,
                        "message": "Video is already in favorites.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                {
                    "success": True,
                    "message": "Video added to favorites.",
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
    
class ListFavoritesAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        favorites = Favorite.objects.filter(
            user=request.user
        ).select_related("video")

        serializer = FavoriteSerializer(
            favorites,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": favorites.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    
class RemoveFavoriteAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, video_id):

        favorite = Favorite.objects.filter(
            user=request.user,
            video_id=video_id,
        ).first()

        if not favorite:

            return Response(
                {
                    "success": False,
                    "message": "Favorite not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        favorite.delete()

        return Response(
            {
                "success": True,
                "message": "Favorite removed successfully.",
            },
            status=status.HTTP_200_OK,
        )
