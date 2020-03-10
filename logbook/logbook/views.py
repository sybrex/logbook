from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Story, Topic
from .services import get_menu


def latest_stories(request):
    menu = get_menu()
    return render(request, 'latest_stories.html', {'menu': menu})


def topic_stories(request, id):
    menu = get_menu()
    topic = Topic.objects.get(pk=id)
    stories = Story.objects.filter(topic=topic)
    return render(request, 'topic_stories.html', {'menu': menu, 'topic': topic, 'stories': stories})
