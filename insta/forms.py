from django import forms
from .models import Profile,Image,Comments

    
class ProfileForm(forms.ModelForm):
    '''
    class to define profile form
    '''
    class Meta:
        model = Profile
        exlcude = ['follower_user', 'following_user']
        fields = ('bio', 'profile_photo')
        