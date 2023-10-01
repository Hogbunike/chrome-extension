from django.shortcuts import render
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer

# Create your views here.

class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer