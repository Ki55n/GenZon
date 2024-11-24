import ast

from django.template.context_processors import request
from rest_framework import serializers
from user import models as user_models
from api import models as api_models


class UserRegisterSerializer(serializers.ModelSerializer):
    """user register serializer"""
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """validate attributes is valid or not"""
        print('attrs: ', attrs)
        return attrs

    def create(self, validated_data):
        user = user_models.User.objects.get_or_create(
            name=validated_data['name'],
            email=validated_data['email'].lower(),
            password=validated_data['password']
        )
        user = user[0]
        return user

    class Meta:
        model = user_models.User
        fields = ["name", "email", "password" ]


class UserLoginSerializer(serializers.ModelSerializer):
    """user login serializer"""
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = user_models.User
        fields = ["email", "password"]

class UserProfileSerializer(serializers.ModelSerializer):
    """user profile serializer"""

    class Meta:
        model = user_models.User
        fields = ["id", "name", "email", "contact_number", ]
