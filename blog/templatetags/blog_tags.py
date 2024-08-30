from django import template
from blog.models import Post1
from blog.models import categorys

register=template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts=Post1.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts=Post1.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('blog/blog-latestpost.html')
def latestposts(arg=3):
    posts=Post1.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-postCategories.html')
def postcategories():
    posts=Post1.objects.filter(status=1)
    categories=categorys.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict}