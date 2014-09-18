import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as auth_user

class Users(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField()
    

class BlogPost(models.Model):
    
    def __str__(self):
        return self.heading
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - \
                                        datetime.timedelta(days=1)
                                        
                                        
    ide = models.IntegerField(primary_key=True)
    paragraph = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    heading = models.CharField(max_length=500)
    authors = models.ManyToManyField(auth_user)
    date_published = models.DateTimeField('date published')
    date_modified = models.DateTimeField('date edited')
   
    
class Paragraphs(models.Model):
    paragraph = models.CharField(max_length=1000)
    post = models.ForeignKey(BlogPost)
    #First paragraph in article will have order=1 and so on
    order = models.IntegerField()
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()
    tags = models.CharField(max_length=100)


class Comments(models.Model):
    
    def __str__(self):
        return self.comment
    
    comment = comment = models.CharField(max_length=1000)
    post = models.ForeignKey(BlogPost)
    paragraph = models.ForeignKey(Paragraphs)
    user = models.ForeignKey(Users)
    date = models.DateTimeField()


class Messages(models.Model):
    
    def __str__(self):
        return self.message
        
    message = models.CharField(max_length=5000)
    user = models.ForeignKey(Users)
    date = models.DateTimeField()
    
    
    
    

