from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect
from .forms import PostForm
from django.contrib.auth.models import User

def post_list(request):
    posts = Post.objects.all().order_by()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)

def post_form(request):

    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            post = Post.objects.create(
                author=author,
                title = title,
                text = text
            )
            return redirect('/post')
    context = {
        'form': form
    }
    print(request.method)
    return render(request, 'post/post_form.html', context)