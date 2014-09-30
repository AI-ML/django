from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User
from blog.models import *

class BlogTests( TestCase ):
    
    def test_urls(self):
        #Testing for url mapping
        c = Client()
        #Testing for get request
        response = c.get('/blog/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/p/contact')
        self.assertEqual(response.status_code, 200)
        response = c.get('/blog/add')
        self.assertEqual(response.status_code, 302)
        response = c.get('/blog/login')
        self.assertEqual(response.status_code, 200)
        response = c.get('/blog/post/')
        self.assertEqual(response.status_code, 404)
        
    def test_views(self):
        #Testing views functionality
        c = Client()
        #Creating a User object to test login process
        user = User.objects.create(username='dummy')
        user.set_password('newpassword')
        user.save()
        #Testing login
        response = c.post('/blog/login', \
                    {'username':'dummy', 'password':'newpassword'})
        self.assertEqual(response.status_code, 302)
        response = c.get('/blog/add')
        self.assertEqual(response.status_code, 200)
        
        #Create a BlogPost object using add_post view function
        response = c.post('/blog/add', {'id_':0, 'heading':'Test Post',\
                            'url':'test','paragraph':'This is a test post',\
                            'order':0, 'tags':'Test'})
        self.assertEqual(response.status_code, 200)
        
        #Test for post url.
        response = c.get('/blog/post/test')
        self.assertEqual(response.status_code, 200)
        
        #Test contact view function for POST request
        response = c.post('/p/contact', {'name':'salil',\
                                'email':'salil@dfordata.com','message':'Hi'})
        self.assertEqual(response.status_code, 200)
        
        
        
        
