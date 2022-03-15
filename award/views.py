from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Rating
from .forms import ProfileForm, NewPostForm, ProjectRatingForm
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

# Create your views here.
