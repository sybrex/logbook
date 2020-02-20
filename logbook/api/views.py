from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from logbook.models import User, Topic, Story
from .serializers import UserSerializer, TopicListSerializer, TopicSerializer, StorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Topic.objects.all()
        serializer = TopicListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Topic.objects.all()
        topic = get_object_or_404(queryset, pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
