from django.shortcuts import render
<<<<<<< HEAD
"""
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html', context={
                      'title': '我的博客首页', 
                      'welcome': '欢迎访问我的博客首页'
                  })
"""
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
=======

# Create your views here.
>>>>>>> 35cf7db8f427b52f09b1e65953fda92a1a0d453e
