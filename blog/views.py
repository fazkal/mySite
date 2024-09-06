from django.shortcuts import render,get_object_or_404
from blog.models import Post1
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def blog_view(requests,**kwargs):
    posts=Post1.objects.filter(status=1)
    if kwargs.get('cat_name')!=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts=posts.filter(author__username=kwargs['author_username'])
    posts=Paginator(posts,2)
    try:
        page_number=requests.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
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

def blog_search(request):
    posts=Post1.objects.filter(status=1) 
    if request.method=='GET':
        if s := request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts' : posts}
    return render(request,'blog/blog-home.html',context)