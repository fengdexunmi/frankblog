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
    url(r"^$", views.main),
    url(r'^post/(?P<pid>\d+)/', views.show_post, name='show_post'),  # 根据文章链接显示文章
    url(r'^tag/(?P<tag>.+)/$', views.list_post_by_tag),  # 根据标签显示相关文章 add by frank at 2014.1.16
    # url(r'^comments/', include('django.contrib.comments.urls')),  # 添加评论模块 add by frank at 2014.2.6
    url(r'^category/(?P<category>.+)/$', views.list_post_by_category),  # 根据分类子节点显示相关文章
    url(r'^(?P<root>.+)/$', views.list_post_by_root),  # 根据分类根节点显示相关文章
)
