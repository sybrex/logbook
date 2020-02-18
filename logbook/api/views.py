from django.http import JsonResponse
from logbook.models import User


def users(request):
    users = User.objects.filter(status=User.STATUS_ACTIVE).values('id', 'name', 'phone')
    data = {
        'status': True,
        'users': list(users)
    }
    return JsonResponse(data)


def user_details(request, id):
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
