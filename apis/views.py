from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def hello(request):
    name = request.GET.get('name', 'guest')
    data = {
        'name': name,
        'message': f"Hello {name}, at the heart of this mission we are solving intelligence to advance science and benefit humanity!"
    }
    return Response(data, status=status.HTTP_200_OK)