#coding=utf8

from django.conf.urls import patterns, include, url
from blog import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frankblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r"^$", views.main),
    (r'^post/(?P<pid>\d+)/', views.show_post),  # 根据文章链接显示文章
    (r'^tag/(?P<tag>.+)/$', views.list_post_by_tag),  # 根据标签显示相关文章 add by frank at 2014.1.16

)
