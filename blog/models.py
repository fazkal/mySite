from django.db import models

# Create your models here.

class Post1 (models.Model):
    title= models.CharField(max_length=30)
    content=models.TextField()
    content_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)