from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer

class RegisterAPIView(APIView):

    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        if serializer.is_valid():

            user = serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "User registered successfully.",
                    "data": {
                        "id": user.id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                    }
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "success": False,
                "message": "Registration failed.",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )