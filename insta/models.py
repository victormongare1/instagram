from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    '''
    profile class to define profile objects
    '''
    profile_pic=models.ImageField(upload_to = 'images/')
    bio=models.CharField(max_length = 100)

class Image(models.Model):
    '''
    image class to define image objects
    '''
    image=models.ImageField(upload_to = 'images/')
    name=
    caption=
    profile=
    likes=
    comments=
