# coding=utf8
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# 标签模型
# add by frank at 2014.1.16 begin #
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='标签')

    def __unicode__(self):
        return self.name

    def get_tag_url(self):
        return '/tag/%s' % self.name

    class Meta:
        verbose_name_plural = '标签'

# add by frank at 2014.1.16 end #


class Post(models.Model):
    title = models.CharField(max_length=60, verbose_name='标题')  # 文章标题
    author = models.ForeignKey(User, verbose_name='作者')  # 作者
    slug = models.CharField(max_length=50, null=True, verbose_name='文章链接',
                            help_text='可包含字母、数字、连字符、下划线')  # 文章链接
    tags = models.ManyToManyField(Tag, null=True, verbose_name='标签')  # 标签 add by frank at 2014.1.16
    content = models.TextField(verbose_name='内容')  # 文章内容
    create_time = models.DateTimeField(auto_now_add=True)  # auto_now_add是对象第一次被创建的时间

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return u'post/%s/%s' % (self.id, self.slug)

    class Meta:
        verbose_name_plural = '文章'