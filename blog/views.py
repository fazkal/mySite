from django.shortcuts import render,get_object_or_404
from blog.models import Post1

def blog_view(requests):
    posts=Post1.objects.filter(status=1)
    context={'posts' : posts}
    return render(requests,'blog/blog-home.html',context)

def blog_single(requests,pid):
    posts=Post1.objects.filter(status=1)
    post=get_object_or_404(Post1,pk=pid)
    context={'post': post}
    return render(requests,'blog/blog-single.html',context)

def test(requests):
    return render(requests,'test.html')

def blog_category(requssts,cat_name):
    posts=Post1.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts}
    return render(requssts,'blog/blog-home.html',context)