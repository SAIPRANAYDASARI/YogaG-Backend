from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.password_validation import validate_password

from profiles.models import Profile

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

        profile.objects.create(
            user=user
        )
        return user
    

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        email = attrs.get("email").lower()

        password = attrs.get("password")

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password."
            )

        attrs["user"] = user

        return attrs
    
class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    def save(self):

        refresh_token = self.validated_data["refresh"]

        token = RefreshToken(refresh_token)

        token.blacklist()

class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate(self, attrs):

        email = attrs.get("email").lower()

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                "No account found with this email."
            )

        token = PasswordResetTokenGenerator().make_token(user)

        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )

        attrs["user"] = user
        attrs["token"] = token
        attrs["uid"] = uid

        return attrs
    
class ResetPasswordSerializer(serializers.Serializer):

    uid = serializers.CharField()

    token = serializers.CharField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        try:

            user_id = urlsafe_base64_decode(
                attrs["uid"]
            ).decode()

            user = User.objects.get(pk=user_id)

        except Exception:

            raise serializers.ValidationError(
                "Invalid reset link."
            )

        token_generator = PasswordResetTokenGenerator()

        if not token_generator.check_token(
            user,
            attrs["token"]
        ):

            raise serializers.ValidationError(
                "Invalid or expired token."
            )

        validate_password(attrs["password"], user)

        attrs["user"] = user

        return attrs

    def save(self):

        user = self.validated_data["user"]

        user.set_password(
            self.validated_data["password"]
        )

        user.save()

        return user