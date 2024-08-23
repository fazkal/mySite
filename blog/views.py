from django.shortcuts import render,get_object_or_404
from blog.models import Post1

def blog_view(requests):
    posts=Post1.objects.filter(status=1)
    context={'posts' : posts}
    return render(requests,'blog/blog-home.html',context)

def blog_single(requests,pid):
    post=get_object_or_404(Post1,pk=pid)
    context={'post': post}
    return render(requests,'blog/blog-single.html',context)