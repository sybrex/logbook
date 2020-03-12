from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Story, Topic
from .services import get_menu


def latest_stories(request):
    menu = get_menu()
    stories = Story.objects.all()
    paginator = Paginator(stories, 4)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'latest_stories.html', {'menu': menu, 'stories': data})


def topic_stories(request, id):
    menu = get_menu()
    topic = Topic.objects.get(pk=id)
    stories = Story.objects.filter(topic=topic)
    paginator = Paginator(stories, 4)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request, 'topic_stories.html', {'menu': menu, 'topic': topic, 'stories': data})
