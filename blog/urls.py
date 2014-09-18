from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.blog, name='blog'),
    url(r'^contact$', views.contact_us, name='contact_us'),
    url(r'^add$', views.add_post, name='add_post'),
    url(r'^login$', views.login, name='login'),
    url(r'^post/(?P<posturl>.*)$', views.post, name='post'),
)
