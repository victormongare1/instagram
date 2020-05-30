from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comments
from django.contrib.auth.models import User
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .forms import ImageForm,ProfileForm,CommentForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts=Image.objects.all()
    return(request, 'Index.html',{"posts":posts})

@login_required(login_url='/accounts/login/')  
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users =Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    

@login_required(login_url='/accounts/login/')  
def profile(request):
    def profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'profile.html',{"form":form})

@login_required(login_url='/accounts/login/')  
def new_post(request):
    post=None

@login_required(login_url='/accounts/login/')  
def new_comment(request,id):
    



