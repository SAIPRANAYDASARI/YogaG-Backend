from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ["user"]

    def validate_age(self, value):
        if value is not None and (value < 10 or value > 100):
            raise serializers.ValidationError(
                "Age must be between 10 and 100."
            )
        return value

    def validate_height(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError(
                "Height must be positive."
            )
        return value

    def validate_weight(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError(
                "Weight must be positive."
            )
        return value