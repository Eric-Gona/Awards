from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Rating
from .forms import ProfileForm, NewPostForm, ProjectRatingForm
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts':posts})
     


@login_required(login_url='/accounts/login/')
def profile(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if new_profile.is_valid():
            new_profile.save()
            return redirect('profile')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', locals())
