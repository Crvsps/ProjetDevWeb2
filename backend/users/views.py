from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import  RegisterSerializer, UserSerializer, UserProfileSerializer
import json


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': UserSerializer(user).data,  
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        profile = request.user.profile 
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        
        profile = request.user.profile

        user_data_raw = request.data.get('user')
        if isinstance(user_data_raw, str):
            try:
                user_data = json.loads(user_data_raw)
            except json.JSONDecodeError:
                return Response({'user': 'Format JSON invalide.'}, status=400)
        else:
            user_data = user_data_raw

        profile_data = request.data.copy()
        profile_data.pop('user', None)
        
        if profile_data.get('photo') in [None, '', 'null', ['null']]:
            profile_data.pop('photo', None)

        profile_serializer = UserProfileSerializer(profile, data=profile_data, partial=True)
        if profile_serializer.is_valid():
            profile_serializer.save()

            user = request.user
            user_serializer = UserSerializer(user, data=user_data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(profile_serializer.data, status=200)
            else:
                return Response({'user': user_serializer.errors}, status=400)
        else:
            return Response(profile_serializer.errors, status=400)


        
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': 'Vous êtes authentifié !',
            'user': request.user.username
        })