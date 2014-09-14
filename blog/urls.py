from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.blog, name='blog'),
    url(r'^contact$', views.contact_us, name='contact_us')
    url(r'^add$', view.add_post, name='add_post')
)
