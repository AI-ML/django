from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from blog.models import *
from blog.forms import *


def blog(request):
    blog_posts = BlogPost.objects.all()
    template = loader.get_template('blog/index.html')
    form = CommentForm()
    context = RequestContext(request, {
        'blog_posts': blog_posts, 'form': form,
    })
    return HttpResponse(template.render(context))

def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            useremail = form.cleaned_data['email']
            
            #retrieving a Users object
            user = Users.objects.get(email=useremail)
            
            formurl = form.cleaned_data['url']
            formheading = form.cleaned_data['heading']
            
            #create a BlogPost object
            blogpost = BlogPost.objects.create(url=formurl,\
                                         heading=formheading )
            blogpost.date_published = datetime.date.today()
            blogpost.date_modified = datetime.date.today()
            blogpost.authors.add(user)
            
            formpara = form.cleaned_data['paragraph']
            #create a Paragraph object
            para = Paragraphs.objects.create(paragraph = formpara,\
                                            post=blogpost)
            para.date_published = datetime.date.today()
            para.date_modified = datetime.date.today()

    
def contact_us(request):
    # if this is a POST request we need to process the form data
    form_uploaded = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            c = Users( name=form.cleaned_data['your_name'],\
                          email=form.cleaned_data['your_email'],\
                          message=form.cleaned_data['your_message'])
            
            c.save()
            form_uploaded = True
        else:
            print 'Data invalid'
     
    form = ContactForm()
     
    return render(request, 'blog/contact.html',{'form': form,\
                                    'form_uploaded':form_uploaded})
        
        
        
        
        
        
        
        
