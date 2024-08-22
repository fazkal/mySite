from django.contrib import admin
from blog.models import Post1

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','content_view','status','published_date','created_date')
    list_filter=('status',)
    ordering=['created_date']
    search_fields=['title','content']
admin.site.register(Post1,PostAdmin)
