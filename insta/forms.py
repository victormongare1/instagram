from django import forms
from .models import Profile,Image,Comments

    
class ProfileForm(forms.ModelForm):
    '''
    class to define profile form
    '''
    class Meta:
        model = Profile
        exlcude = ['user']
        fields = ('bio', 'profile_pic')
         
class ImageForm(forms.ModelForm):
    '''
    class to define image uploading form
    '''
    class Meta:
        model = Image
        exclude = ['profile','likes']
        fields = ('image','name','caption')  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'user']
        fields = ('comment',)
                 