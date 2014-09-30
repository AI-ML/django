from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import View

from blog.models import *
from blog.forms import *


def blog(request):
    blog_posts = BlogPost.objects.order_by('ide')
       
    return render(request, 'blog/bloghome.html',
                                         {'blog_posts': blog_posts})

def add_post(request):
    
    # If not an Authenticated user, redirects to login page
    if not request.user.is_authenticated(): 
        return HttpResponseRedirect('/p/login')
    
    form = AddPostForm(request.POST)
    
    if request.method == 'POST' and form.is_valid():
                
            posturl = form.cleaned_data['url']
            postheading = form.cleaned_data['heading']
            identifier = form.cleaned_data['id_']
            date = datetime.date.today()
            #create a BlogPost Object or get one
            try:
                blogpost = BlogPost.objects.get(ide=identifier)
            except ObjectDoesNotExist:
                blogpost = BlogPost.objects.create(ide=identifier,\
                                date_published=date, date_modified=date)
            
            blogpost.url = posturl
            blogpost.heading = postheading
            blogpost.date_modified = date
            blogpost.authors.add(request.user)
            blogpost.save()
            
            paragraph = form.cleaned_data['paragraph']
            order = form.cleaned_data['order']
            tags = form.cleaned_data['tags']
            
            #First para of a post also saved in BlogPost table
            if order == 0:
                blogpost.paragraph = paragraph
            
            blogpost.save()   
            #get or create a Paragraph object
            try:
                para = Paragraphs.objects.get(post=blogpost,\
                                              order=order)
            except ObjectDoesNotExist:
                para = Paragraphs.objects.create(post=blogpost,order=order,\
                                    date_published=date,date_modified=date)
            
            para.paragraph = paragraph
            para.date_modified = date
            para.tags = tags
            para.save()
    
    return render(request, 'blog/add_post.html',{'form': form})


def post(request, posturl):
    try:
        blogpost = BlogPost.objects.get(url=posturl)
        paras = Paragraphs.objects.filter(post=blogpost).\
                                                    order_by('order')
        
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'blog/post.html', {'paras':paras,\
                                              'blogpost':blogpost})
    
                
def login(request):
    
    form = LoginForm(request.POST)
    
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            #redirects to new url
            return HttpResponseRedirect('/blog/add')
        
    return render(request, 'blog/login.html',{'form': form})    
    
    
    
    
def contact_us(request):
    # if this is a POST request we need to process the form data
    form_uploaded = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            date = datetime.date.today()
            user = Users.objects.create(name=form.cleaned_data['name'],\
                          email=form.cleaned_data['email'],date=date)
                          
            message = Messages.objects.create(user=user,date=date,\
                                        message=form.cleaned_data['message'])
            
            form_uploaded = True
            print 'Data valid'
        else:
            print 'Data invalid'
     
    form = ContactForm()
     
    return render(request, 'blog/contact.html',{'form': form,\
                                    'form_uploaded':form_uploaded})
        
        
        
        
        
        
        
        
