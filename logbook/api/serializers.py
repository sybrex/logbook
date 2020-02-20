from rest_framework import serializers
from logbook.models import User, Topic, Story


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'status']


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'created']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'type', 'description', 'topic', 'user', 'content', 'created']
        depth = 1


class TopicStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'type', 'description', 'user', 'content', 'created']
        depth = 1


class TopicSerializer(serializers.ModelSerializer):
    stories = TopicStorySerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'created', 'stories']
        depth = 1
