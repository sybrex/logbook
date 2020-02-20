from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import UserSerializer, TopicSerializer, StorySerializer
from logbook.models import User, Topic, Story


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
