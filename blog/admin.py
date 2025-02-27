from django.contrib import admin
from blog.models import Post1,categorys,comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','author','content_view','status','published_date','created_date')
    list_filter=('status','author')
    ordering=['created_date']
    search_fields=['title','content']
    summernote_fields=('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('name','post','approved','created_date')
    list_filter=('post','approved')
    ordering=['created_date']
    search_fields=['name','post']

admin.site.register(comment,CommentAdmin)
admin.site.register(Post1,PostAdmin)
admin.site.register(categorys)
