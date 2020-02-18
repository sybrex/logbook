from django.http import JsonResponse
from django.core.serializers import serialize
from logbook.models import User


def users(request):
    users = User.objects.all()
    return JsonResponse(serialize('json', users), safe=False)
