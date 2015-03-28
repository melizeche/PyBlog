from django.conf.urls import patterns, include, url
from django.contrib import admin
#from blog import views

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'blog.views.home', name='home'),
    url(r'^post$', 'blog.views.posts', name='posts'),
    url(r'^add$', 'blog.views.add', name='add'),
    url(r'^$', 'blog.views.lista', name='lista'),
    url(r'^post/(?P<post_id>\d+)/$', 'blog.views.post', name='post'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
