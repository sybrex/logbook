from django.db import models
from . import services


class User(models.Model):

    class Meta:
        db_table = 'users'

    STATUS_ACTIVE = 1
    STATUS_DISABLED = 2
    STATUSES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_DISABLED, 'Disabled')
    ]

    telegram_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=50, default='')
    status = models.IntegerField(choices=STATUSES, default=STATUS_ACTIVE)

    def __str__(self):
        return f'{self.telegram_id}'


class Topic(models.Model):

    class Meta:
        db_table = 'topics'
        ordering = ['-created']

    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Story(models.Model):

    class Meta:
        db_table = 'stories'
        verbose_name_plural = 'stories'
        ordering = ['-created']

    TYPE_IMAGE = 1
    TYPE_ALBUM = 2
    TYPE_VIDEO = 3
    TYPE_TEXT = 4
    MEDIA_TYPES = [
      (TYPE_IMAGE, 'Image'),
      (TYPE_ALBUM, 'Album'),
      (TYPE_VIDEO, 'Video'),
      (TYPE_TEXT, 'Text')
    ]

    type = models.IntegerField(choices=MEDIA_TYPES, default=TYPE_IMAGE)
    description = models.TextField(default='')
    topic = models.ForeignKey(Topic, related_name='stories', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    content = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        if self.type == self.TYPE_IMAGE:
            img = services.download_image(self.content)
            self.content = img
        super(Story, self).save(*args, **kwargs)

    def __str__(self):
        return f'Story {self.type}'
