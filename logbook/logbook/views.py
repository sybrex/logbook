from django.shortcuts import render


def latest_stories(request):
    return render(request, 'latest_stories.html')


def topic_stories(request, topic):
    return render(request, 'topic_stories.html')
