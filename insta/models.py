from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    '''
    profile class to define profile objects
    '''
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to = 'images/')
    bio=models.CharField(max_length = 100)

    def __str__(self):
        return self.user

    @classmethod
    def search_by_name(cls,search_term):
        '''
        method that rerieves a user by use of username
        '''
        name = cls.objects.filter(user__username__icontains = search_term)
        return name

class Image(models.Model):
    '''
    image class to define image objects
    '''
    image=models.ImageField(upload_to = 'images/')
    name=models.CharField(max_length = 100)
    caption=models.CharField(max_length = 100)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    comments=models.CharField(max_length = 100)
    
    def __str__(self):
        '''
        Setting up self
        '''
        return self.name

    def save_image(self):
        '''
        method that saves post to database
        '''
        self.save()

    def delete_image(self):
        '''
        method that deletes post from database
        '''
        self.delete()    
        