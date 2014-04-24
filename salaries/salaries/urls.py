from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'people.views.home', name='home'),
    url(r'^person/(?P<slug>[-\w]+)/$', 'people.views.personDetail', name='persondetail'),
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
