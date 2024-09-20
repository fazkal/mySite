from django.shortcuts import render,get_object_or_404
from blog.models import Post1,comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def blog_view(requests,**kwargs):
    posts=Post1.objects.filter(status=1)
    if kwargs.get('cat_name')!=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts=posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name')!=None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])
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
    if requests.method=='POST':
        form=CommentForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.add_message(requests,messages.SUCCESS,'Your comment has been submited.')
        else:
            messages.add_message(requests,messages.ERROR,'Your comment failed.')
    posts=Post1.objects.filter(status=1)
    post=get_object_or_404(Post1,pk=pid)
    if  post.login_require==False or requests.user.is_authenticated:
        comments=comment.objects.filter(post=post.id,approved=True)
        form=CommentForm()
        context={'post': post,'comments':comments,'form':form}
        return render(requests,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

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