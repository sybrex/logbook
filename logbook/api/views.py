from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from logbook.models import User, Topic, Story
from .serializers import UserSerializer, TopicListSerializer, TopicSerializer, StorySerializer, StoryListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def list(self, request):
        serializer = TopicListSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        topic = get_object_or_404(self.queryset, pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def list(self, request):
        serializer = StoryListSerializer(self.queryset, many=True)
        return Response(serializer.data)
