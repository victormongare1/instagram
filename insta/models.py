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
    followers= models.IntegerField(blank=True , null=True)
    following = models.IntegerField(blank=True, null=True)

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
    caption=models.CharField(max_length = 100,blank=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    
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

class Comments(models.Model):
    '''
    Comment class for comment objects
    '''
    comment= models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    image_id=models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        '''
        Setting up self
        '''
        return self.comment

    @classmethod
    def get_comments(cls):
        '''
        Method for getting all the comments posted
        '''
        comment=cls.objects.all()
        return comment

    @classmethod
    def get_singlepost_comments(cls, id):
        '''
        function that gets comments for a single post
        '''
        comments=cls.objects.filter(image_id=id)
        return comments
    def save_comment(self):
        '''
        function that saves a new comment
        '''
        self.save()

    def delete_comment(self):
        '''
        function that deletes a comment
        '''
        self.delete()        
