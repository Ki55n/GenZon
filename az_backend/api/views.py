import json
import random

from django.contrib.auth import authenticate
from django.utils.translation import trim_whitespace
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api import serializers


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            messages: dict = {}
            for key, value in dict(serializer.errors).items():
                messages[key] = value[0]

            return Response(data={
                'success': False,
                'message': list(messages.values())[0],
            })

        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response(data={
            'success': True,
            'message': 'Successfully registered.',
            'data': {
                'tokens': tokens,
            }
        })


class UserLoginView(generics.CreateAPIView):
    serializer_class = serializers.UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            messages: dict = {}
            for key, value in dict(serializer.errors).items():
                messages[key] = value[0]
            return Response(data={'messages': messages, 'status': {'msg': 'failed', 'code': 220}})
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response(
                {'token': token, 'message': 'Login Successful.', 'status': {'msg': 'success', 'code': 200}},
                status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Email or Password is not Valid',
                             'status': {'msg': 'success', 'code': 230}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = serializers.UserProfileSerializer(data=request.data)
        return Response({
            'success': True,
            'message': 'Successfully retrieved.',
            'data': serializer.data,
        })

class UserLogoutView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Blacklist the refresh token
            refresh_token = request.data.get("refresh")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({"message": "Logged out successfully."}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)
