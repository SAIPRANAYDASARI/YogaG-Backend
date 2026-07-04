from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from profiles.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password":
                    "Passwords do not match."
                }
            )

        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        Profile.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(
                refresh.access_token
            ),
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self):
        token = RefreshToken(
            self.token
        )

        token.blacklist()


class ForgotPasswordSerializer(
    serializers.Serializer
):
    email = serializers.EmailField()

    def validate_email(
        self,
        value
    ):
        if not User.objects.filter(
            email=value
        ).exists():

            raise serializers.ValidationError(
                "User with this email does not exist."
            )

        return value


class ResetPasswordSerializer(
    serializers.Serializer
):
    user_id = serializers.IntegerField()
    token = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.get(
            id=attrs["user_id"]
        )

        if not default_token_generator.check_token(
            user,
            attrs["token"]
        ):
            raise serializers.ValidationError(
                "Invalid token."
            )

        attrs["user"] = user

        return attrs

    def save(self):
        user = self.validated_data["user"]

        user.set_password(
            self.validated_data["password"]
        )

        user.save()