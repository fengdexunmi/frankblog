# coding=utf8
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='标题')  # 文章标题
    author = models.ForeignKey(User, verbose_name='作者')  # 作者
    slug = models.CharField(max_length=50, db_index=True, verbose_name='文章链接',
                            help_text='可包含字母、数字、连字符、下划线')  # 文章链接
    content = models.TextField(verbose_name='内容')  # 文章内容
    create_time = models.DateTimeField(auto_now_add=True)  # auto_now_add是对象第一次被创建的时间

    def __unicode__(self):
        return self.title

    def get_post_url(self):
        return '/%s' % self.slug

    class Meta:
        verbose_name_plural = '文章'
