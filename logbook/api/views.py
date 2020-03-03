from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from django.shortcuts import get_object_or_404
from logbook.models import User, Topic, Story
from .serializers import UserSerializer, TopicListSerializer, TopicSerializer, StorySerializer, StoryListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']

    def retrieve(self, request, pk=None):
        topic = get_object_or_404(self.queryset, pk=pk)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def list(self, request):
        queryset = Story.objects.all()
        topic_id = request.query_params.get('topic', None)
        if topic_id is not None:
            queryset = queryset.filter(topic_id=int(topic_id))
        serializer = StoryListSerializer(queryset, many=True)
        return Response(serializer.data)
