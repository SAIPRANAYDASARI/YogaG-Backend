from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        source="user.first_name",
        read_only=True
    )

    last_name = serializers.CharField(
        source="user.last_name",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "email",
            "profile_image",
            "date_of_birth",
            "gender",
            "height",
            "weight",
            "fitness_level",
            "fitness_goal",
            "medical_conditions",
            "bio",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]