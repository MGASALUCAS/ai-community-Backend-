from django.urls import path
from .views import SignupView, SigninView, UpdateProfileView, ForgotPasswordView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
]
