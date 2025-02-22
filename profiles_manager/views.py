from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .serializers import SignupSerializer, SigninSerializer, UpdateProfileSerializer, ForgotPasswordSerializer

User = get_user_model()

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

class SigninView(generics.GenericAPIView):
    serializer_class = SigninSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        
        response_data = {
            'id': str(user.id),
            'fullName': user.username,
            'emailAddress': user.email,
            'avatar': user.profile.avatar if hasattr(user, 'profile') else None,
            'sex': user.gender if hasattr(user, 'profile') else None,
            'token': str(refresh.access_token),
            'role': [
                {
                    'name': user.role,
                    'permissions': [
                        'view-dashboard',
                        'create-user',
                    ],
                },
            ],
        }
        
        return Response(response_data, status=status.HTTP_200_OK)

class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.validated_data['email']).first()
        if user:
            # Send reset link (mock implementation)
            send_mail(
                'Password Reset',
                'Click the link to reset your password.',
                'noreply@example.com',
                [user.email],
                fail_silently=False,
            )
        return Response({"message": "If your email exists, you will receive a password reset link."}, status=status.HTTP_200_OK)
