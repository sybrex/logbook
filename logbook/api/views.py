from django.http import JsonResponse
from logbook.models import User, Topic, Story


def get_users(request):
    users = User.objects.filter(status=User.STATUS_ACTIVE).values('id', 'name', 'phone')
    data = {
        'status': True,
        'users': list(users)
    }
    return JsonResponse(data)


def get_user(request, id):
    try:
        user = User.objects.get(pk=id)
        data = {
            'status': True,
            'user': {
                'name': user.name,
                'phone': user.phone,
                'status': user.status
            }
        }
    except User.DoesNotExist:
        data = {
            'status': False,
            'error_message': f'User {id} not found'
        }
    return JsonResponse(data)


def get_greetings(request):
    pass


def get_topics(request):
    pass


def get_topic(request, id):
    pass


def create_topic(request):
    pass


def update_topic(request):
    pass


def remove_topic(request, id):
    pass


def get_story(request, id):
    pass


def create_story(request):
    pass


def update_story(request):
    pass


def remove_story(request, id):
    pass
