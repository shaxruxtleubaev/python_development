from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(pubDate__lte=timezone.now().order_by('pubDate'))
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)
