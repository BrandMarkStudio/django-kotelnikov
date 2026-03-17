from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'blog.views.home', name='home'),
    url(r'^article/(?P<article_id>\d+)$','articles.views.get_article',name='get_article'),
    # url(r'^blog/', include('blog.foo.urls')),
    url(r'^$', 'articles.views.archive', name='archive'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
