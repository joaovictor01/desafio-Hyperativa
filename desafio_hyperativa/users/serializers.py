from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # noqa: F811


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "email")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already in use!")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
