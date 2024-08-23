from django.shortcuts import render
from blog.models import Post1

def blog_view(requests):
    posts=Post1.objects.filter(status=1)
    context={'posts' : posts}
    return render(requests,'blog/blog-home.html',context)

def blog_single(requests):
    return render(requests,'blog/blog-single.html')