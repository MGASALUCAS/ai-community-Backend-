from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Discussion, DiscussionComment, DiscussionLike
from .serializers import DiscussionSerializer, DiscussionCommentSerializer, DiscussionLikeSerializer

class DiscussionViewSet(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated]

class DiscussionCommentViewSet(viewsets.ModelViewSet):
    queryset = DiscussionComment.objects.all()
    serializer_class = DiscussionCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class DiscussionLikeViewSet(viewsets.ModelViewSet):
    queryset = DiscussionLike.objects.all()
    serializer_class = DiscussionLikeSerializer
    permission_classes = [permissions.IsAuthenticated]
