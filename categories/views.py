from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer

class CategoryListAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        categories = Category.objects.filter(
            is_active=True
        )

        serializer = CategorySerializer(
            categories,
            many=True,
        )

        return Response(
            {
                "success": True,
                "count": categories.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

