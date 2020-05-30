from django.shortcuts import render
from django.contrib.auth.decorators import login_required.
from .models import Image,Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts=Image.objects.all()
    return(request, 'Index.html',{"posts":posts})

@login_required(login_url='/accounts/login/')  
def search_results(request):
    search=None

@login_required(login_url='/accounts/login/')  
def profile(request):
    profile=None

@login_required(login_url='/accounts/login/')  
def new_post(request):
    post=None



