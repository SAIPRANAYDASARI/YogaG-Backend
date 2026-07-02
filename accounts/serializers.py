from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def validate_email(self, value):
        email = value.lower()

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "A user with this email already exists."
            )

        return email


    def create(self, validated_data):
        password = validated_data.pop("password")
        email = validated_data.pop("email")
        user = User(
            username=email,
            email=email,
            **validated_data
            )
        user.set_password(password)
        user.save()
        return user