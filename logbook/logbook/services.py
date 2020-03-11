import requests
import os
import uuid
from django.conf import settings
from PIL import Image
from shutil import copyfileobj
from . import models


def download_image(url):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        ext = url.split('.')[-1]
        base_name = uuid.uuid4().hex + '.' + ext
        full_name = os.path.join(settings.MEDIA_ROOT, 'images/', base_name)
        if not os.path.exists(full_name):
            with open(full_name, 'wb') as out_file:
                copyfileobj(res.raw, out_file)
            resize_image(full_name)
        return base_name


def resize_image(full_name):
    sizes = [640, 750, 1080]
    max_height = 1350
    basename = os.path.basename(full_name)
    for max_width in sizes:
        img = Image.open(full_name)
        img.thumbnail((max_width, max_height), Image.ANTIALIAS)
        img_name = os.path.join(settings.MEDIA_ROOT, 'images/', f'{max_width}_{basename}')
        img.save(img_name, progressive=True, quality=100)


def download_video(url):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        ext = url.split('.')[-1]
        base_name = uuid.uuid4().hex + '.' + ext
        full_name = os.path.join(settings.MEDIA_ROOT, 'videos/', base_name)
        if not os.path.exists(full_name):
            with open(full_name, 'wb') as out_file:
                copyfileobj(res.raw, out_file)
        return base_name


def get_menu():
    topics = models.Topic.objects.all()
    return topics
