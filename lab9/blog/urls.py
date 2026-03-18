from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^article/(?P<article_id>\d+)$', 'articles.views.get_article', name='get_article'),
    url(r'^$', 'articles.views.archive', name='archive'),
    url(r'^article/new/$', 'articles.views.create_post', name='create_post'),
    url(r'^registration/$', 'articles.views.registration', name='registration'),
    url(r'^login/$', 'articles.views.user_login', name='login'),
    url(r'^logout/$', 'articles.views.user_logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
