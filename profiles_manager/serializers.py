from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.socialaccount.models import SocialAccount

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    whatsappNumber = serializers.CharField(source='profile.whatsapp_number', required=False)
    twitter = serializers.URLField(source='profile.twitter', required=False)
    github = serializers.URLField(source='profile.github', required=False)
    linkedIn = serializers.URLField(source='profile.linkedin', required=False)
    instagram = serializers.URLField(source='profile.instagram', required=False)
    sectors = serializers.ListField(child=serializers.CharField(), source='profile.sectors', required=False)
    technologies = serializers.ListField(child=serializers.CharField(), source='profile.technologies', required=False)
    education = serializers.JSONField(source='profile.education', required=False)
    achievements = serializers.JSONField(source='profile.achievements', required=False)
    projects = serializers.JSONField(source='profile.projects', required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'whatsappNumber', 'twitter', 'github', 'linkedIn', 'instagram', 'sectors', 'technologies', 'education', 'achievements', 'projects']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.filter(email=data['email']).first()
        if user and user.check_password(data['password']):
            return user
        raise serializers.ValidationError("Invalid credentials")

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile']

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()