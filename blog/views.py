from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from blog.models import *
from blog.forms import *


def index(request):
    blog_posts = BlogPost.objects.all()
    template = loader.get_template('blog/index.html')
    form = CommentForm()
    context = RequestContext(request, {
        'blog_posts': blog_posts, 'form': form,
    })
    return HttpResponse(template.render(context))
    
def contact_us(request):
    # if this is a POST request we need to process the form data
    form_uploaded = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            c = Contacts( name=form.cleaned_data['your_name'],\
                          email=form.cleaned_data['your_email'],\
                          message=form.cleaned_data['your_message'])
            
            c.save()
            form_uploaded = True
        else:
            print 'Data invalid'
     
    form = ContactForm()
     
    return render(request, 'blog/contact.html',{'form': form,\
                                    'form_uploaded':form_uploaded})
        
        
        
        
        
        
        
        
