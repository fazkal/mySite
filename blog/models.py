from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class categorys(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post1 (models.Model):
    image=models.ImageField(upload_to='blog/',default='blog/Default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title= models.CharField(max_length=30)
    content=models.TextField()
    tags=TaggableManager()
    category=models.ManyToManyField(categorys)
    content_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} - {} ".format(self.title,self.id)
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    
class comment(models.Model):
    post=models.ForeignKey(Post1,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    email=models.EmailField()
    subject=models.CharField(max_length=225)
    message=models.TextField()
    approved=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return self.name