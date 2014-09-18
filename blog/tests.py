from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User

class BlogTests( TestCase ):

    def test_urls(self):
        #Testing status_code for urls.
        c = Client()
        #Testing for get request
        response = c.get('/blog/')
        self.assertEqual(response.status_code, 200)
        response = c.get('/blog/contact')
        self.assertEqual(response.status_code, 200)
        response = c.get('/blog/add')
        self.assertEqual(response.status_code, 302)
        response = c.get('/blog/login')
        self.assertEqual(response.status_code, 200)
        response = c.get('/blog/post/')
        self.assertEqual(response.status_code, 404)
        
        #Creating a User object to test login process
        user = User.objects.create(username='dummy')
        user.set_password('newpassword')
        user.save()
        #Testing post request for login page
        response = c.post('/blog/login', \
                    {'username':'dummy', 'password':'newpassword'})
        self.assertEqual(response.status_code, 302)
        response = c.get('/blog/add')
        self.assertEqual(response.status_code, 200)
        
