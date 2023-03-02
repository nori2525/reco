from django.core.files import storage
from django.db import models
import os
import shutil
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your models here.
class m_user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    dir_path = models.CharField(max_length=200)

class w_user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    dir_path = models.CharField(max_length=200)

class OverwriteStorage(FileSystemStorage): 
     def get_available_name(self, name, max_length=None):
        shutil.rmtree(settings.MEDIA_ROOT)
        os.mkdir(settings.MEDIA_ROOT) 
        return name

fs = OverwriteStorage(location=settings.MEDIA_ROOT)

class user_img(models.Model):
    img1 = models.ImageField(
        verbose_name = 'img_1',
        upload_to = 'images/',
        storage = fs
    )
    img2 = models.ImageField(
        verbose_name = 'img_2',
        upload_to = 'images/',
    )
    img3 = models.ImageField(
        verbose_name = 'img_3',
        upload_to = 'images/',
    )

class single_img(models.Model):
    img = models.ImageField(
        verbose_name = "img_1",
        upload_to = 'SImg/',
        storage = fs
    )