from django.contrib import admin
from .models import User, Topic, Story


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'status')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('created', 'title')


class StoryAdmin(admin.ModelAdmin):
    list_display = ('created', 'type')


admin.site.register(User, UserAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Story, StoryAdmin)
