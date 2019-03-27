from django.shortcuts import render,get_object_or_404,redirect,reverse
from .models import Profile


def ProfileView(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        picture = request.user.picture

    context= {
        'username':username
    }

