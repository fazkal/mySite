
from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    
    #path('url address' , view),
    path('',blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    path('test',test,name='test'),
    path('category/<str:cat_name>',blog_category,name='category'),
    path('tag/<str:tag_name>',blog_view,name='tag'),
    path('author/<str:author_username>',blog_view,name='author'),
    path('search/',blog_search,name='search'),
    
]