from django.shortcuts import render
from rest_framework import generics
from .models import Resource
from .serializers import ResourceSerializer
from rest_framework.permissions import AllowAny

# List all resources or create new one
class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [AllowAny]

# Retrieve, update, or delete a specific resource
class ResourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [AllowAny]
