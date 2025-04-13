from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
    def validate_username(self, value):
        user = self.instance  # l'utilisateur actuel
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà pris.")
        return value

        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    photo = serializers.ImageField(required=False, allow_null=True)  

    class Meta:
        model = UserProfile
        fields = (
            'user',            
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'user_type',
            'photo',
            'points',
        )  
        
    '''
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    '''

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)  

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        UserProfile.objects.create(
            user=user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            points=0 
        )
        return user