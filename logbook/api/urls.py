from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'stories', views.StoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# app_name = 'api'
#
# urlpatterns = [
#     path('users', views.get_users, name='users_list'),
#     path('users/<int:id>', views.get_user, name='user_details'),
#     path('greetings', views.get_greetings, name='greetings_list'),
#     path('topics', views.get_topics, name='topics_list'),
#     path('topics/<int:id>', views.get_topic, name='topic_details'),
# ]
