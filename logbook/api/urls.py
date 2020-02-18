from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('users', views.users, name='users'),
    path('users/<int:id>', views.user_details, name='user_details'),
]
